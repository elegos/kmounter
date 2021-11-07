import re
from dataclasses import dataclass, field
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from pathlib import Path
from typing import List, Optional, Union

import netifaces
from common.actions_pb2 import Mount, MountNFS, Umount
from services import libc
from utils import WhoIs

MS_REMOUNT = 32
MNT_FORCE = 1


class MountException(Exception):
    pass


@dataclass
class Mount:
    source: str
    target: str
    type: str
    options: str
    should_be_dumped: int
    fsck_order: int

    remounted: bool = field(default=False)


def getCurrentMounts() -> List[Mount]:
    result = []

    with open('/proc/mounts', 'r') as fh:
        for line in fh:
            source, target, type, options, shouldBeDumped, fsckOrder = line.split(' ')
            result.append(Mount(source, target, type, options,
                                int(shouldBeDumped), int(fsckOrder)))

    return result


def getMountPath(mountPrefixPath: Path, who: WhoIs, mountName: str) -> Path:
    return mountPrefixPath.joinpath(who.username, mountName)


def getMatchingOwnIPAddress(addr: str) -> Optional[str]:
    addrs = {}
    for interface in netifaces.interfaces():
        iaddrs = netifaces.ifaddresses(interface)
        for key in iaddrs.keys():
            if key not in addrs:
                addrs[key] = []
            addrs[key].extend(iaddrs[key])

    ipv4regex = r'\d+\.\d+\.\d+\.\d+'

    if re.match(ipv4regex, addr):
        addrs = addrs[netifaces.AF_INET]
        for a in addrs:
            a['addr'] = IPv4Address(a['addr'])
            a['netmask'] = IPv4Address(a['netmask'])

            a['network'] = IPv4Address(int(a['addr']) & int(a['netmask'])).exploded
            a['network'] = IPv4Network(f'{a["network"]}/{a["netmask"]}')
    else:
        addrs = addrs[netifaces.AF_INET6]
        for a in addrs:
            a['addr'] = IPv6Address(a['addr'])
            a['prefix_length'] = int(a['netmask'].split('/')[1])
            a['network'] = IPv6Network(a['netmask'])

    targetAddr = IPv4Address(addr) if re.match(ipv4regex, addr) else IPv6Address(addr)
    for a in addrs:
        network: Union[IPv4Network, IPv6Network] = a['network']
        if targetAddr in network:
            return a['addr'].exploded

    return None


def getMount(target: str):
    return next((mount for mount in getCurrentMounts() if mount.target == target), None)


def mountNFS(mountPrefixPath: Path, who: WhoIs, msg: MountNFS) -> Mount:
    '''
    Returns the Mount that has been (re)mounted

    Raises MountException, Exception
    '''
    mountPrefixPath = getMountPath(mountPrefixPath, who, msg.mount_name)

    if not mountPrefixPath.exists():
        mountPrefixPath.mkdir(parents=True)

    mounted = getMount(str(mountPrefixPath))
    if mounted is None or mounted.source != msg.source or not mounted.type.startswith('nfs'):
        mounted = None

    # non-empty directory
    if not mounted and any(mountPrefixPath.iterdir()):
        raise MountException(f"{mountPrefixPath} is not empty, can't mount.")

    options: List[str] = msg.options.split(',') if len(msg.options) else []
    targetIP = msg.source.split(':')[0]
    clientIP = getMatchingOwnIPAddress(targetIP)
    if clientIP is None:
        clientaddr = next(
            (option for option in options if option.startswith('clientaddr=')), None)
        if not clientaddr:
            raise MountException("Can't determine clientaddr, please specify it manually.")
        options.remove(clientaddr)
        clientIP = clientaddr.split('=')[1]

    commonOptions = [f'addr={targetIP}', f'clientaddr={clientIP}']
    nfsOptions = [
        ['vers=4.2', *commonOptions],
        ['vers=4', 'minorversion=1', *commonOptions]
    ]

    returnValue = None
    preMounted = mounted is not None
    for optGroup in nfsOptions:
        optGroup.extend(options)
        returnValue = libc.LIBC.mount(
            msg.source.encode(),
            str(mountPrefixPath).encode(),
            'nfs'.encode(),
            MS_REMOUNT if preMounted else 0,
            ','.join(optGroup).encode(),
        )

        if returnValue == 0:
            break

    errMsg = libc.analyzeExitCode(returnValue, 'mount')
    if errMsg:
        raise MountException(errMsg)

    mounted = getMount(str(mountPrefixPath))
    mounted.remounted = preMounted

    return mounted


def umount(mountPath: Path, msg: Umount) -> Mount:
    mounted = getMount(str(mountPath))

    if not mounted:
        return mounted

    if msg.force:
        exitCode = libc.LIBC.umount2(str(mountPath).encode(), MNT_FORCE)
    else:
        exitCode = libc.LIBC.umount(str(mountPath).encode())

    errMsg = libc.analyzeExitCode(exitCode, 'umount')
    if errMsg:
        raise Exception(errMsg)

    return mounted

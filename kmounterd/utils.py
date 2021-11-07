import socket
import struct
import pwd
import grp
from dataclasses import dataclass


@dataclass
class WhoIs:
    pid: int
    uid: int
    gid: int

    @property
    def username(self) -> str:
        return pwd.getpwuid(self.uid).pw_name

    @property
    def group(self) -> str:
        return grp.getgrgid(self.gid).gr_name

    def __str__(self) -> str:
        return f'{self.pid} - {self.username}:{self.group}'


def whois(sock: socket.socket) -> WhoIs:
    creds = sock.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, struct.calcsize('3i'))
    pid, uid, gid = struct.unpack('3i', creds)

    return WhoIs(pid=pid, uid=uid, gid=gid)

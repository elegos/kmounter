import logging
import os
import pwd
from pathlib import Path
from services import libc

from utils import WhoIs


class HomeSymlinkException(Exception):
    pass


def makeHomeSymlink(who: WhoIs, source: Path, target: Path):
    target = target.expanduser()
    userHome = Path(pwd.getpwuid(who.uid).pw_dir)
    if not userHome:
        raise HomeSymlinkException("Can't detect user's home directory, link not created.")

    if target.is_absolute() and not target.is_relative_to(userHome):
        raise HomeSymlinkException(
            "Home symlink target can only be within the user's home directory, link not created.")

    target = userHome.joinpath(target)

    if target.exists():
        if not target.is_symlink() or target.readlink() != source:
            raise HomeSymlinkException('Symlink target already exists, link not created.')

        return

    target.symlink_to(source, target_is_directory=True)
    exitCode = libc.LIBC.lchown(str(target).encode(), who.uid, who.gid)
    errMsg = libc.analyzeExitCode(exitCode, 'make home symlink')
    if errMsg:
        raise HomeSymlinkException(errMsg)

    logging.info(f'{who} | Created symlink {source} -> {target}')


def unlink(who: WhoIs, source: Path, target: Path):
    target = target.expanduser()
    userHome = Path(pwd.getpwuid(who.uid).pw_dir)
    if not userHome:
        raise HomeSymlinkException("Can't detect user's home directory, path left untouched.")

    if target.is_absolute() and not target.is_relative_to(userHome):
        raise HomeSymlinkException(
            "Home symlink target can only be within the user's home directory, path left untouched.")

    target = userHome.joinpath(target)

    if not target.exists():
        logging.debug(f'{who} | {target} does not exist')
        return

    if not target.is_symlink():
        raise HomeSymlinkException('Given home symlink is not a symlink')

    if not target.readlink() == source:
        raise HomeSymlinkException(
            f'Symlink points to a different directory ({target.readlink()} vs {source})')

    target.unlink()

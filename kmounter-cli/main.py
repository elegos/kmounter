import os
import socket
from argparse import ArgumentParser
from typing import List

from commands import CheckDaemonStatusCommand, Command, MountNFSCommand
from commands.umount import UmountCommand
from common.settings import Settings

args = ArgumentParser()
subParsers = args.add_subparsers(help='Available commands', dest='command')

commands: List[Command] = [CheckDaemonStatusCommand(), MountNFSCommand(), UmountCommand()]

for command in commands:
    command.enrich_args(subParsers)

settings = Settings.fromArgs(args)

try:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(str(settings.socketPath))
except ConnectionRefusedError:
    print('Daemon is not running.')
    os._exit(1)

for command in commands:
    if command.run(settings.args, sock):
        break

sock.close()

from argparse import ArgumentParser, _SubParsersAction
from socket import socket

from google.protobuf.message import Message

from commands.common import Command
from common.actions_pb2 import ActionMessage, MountNFS
from common.const import MessageType
from common.packet import Packet


class MountNFSCommand(Command):
    @staticmethod
    def enrich_args(subParsers: _SubParsersAction) -> None:
        parser: ArgumentParser = subParsers.add_parser('mount-nfs', help='Mount a NFS volume')
        parser.add_argument('source', help='NFS source path')
        parser.add_argument('target', help='Name of the NFS mount (i.e. my_nfs)')
        parser.add_argument('options', nargs='?', default=None, help='Optional mount arguments')
        parser.add_argument(
            '--home-symlink', help="Symlink path relative to the user's home", required=False, default=None)

    def run(self, args: ArgumentParser, sock: socket) -> bool:
        arguments, _ = args.parse_known_args()

        if arguments.command != 'mount-nfs':
            return False

        msg: Message = MountNFS()
        msg.mount_name = arguments.target
        msg.source = arguments.source
        msg.options = arguments.options or ''
        msg.home_sym_link = arguments.home_symlink or ''

        packet = Packet(MessageType.MOUNT_NFS, msg)
        sock.send(packet.serialize())
        response = Packet.read(sock)

        if response.type == MessageType.ERROR:
            rMsg: Message = ActionMessage()
            rMsg.ParseFromString(response.messageBytes)
            print(f'Mount error: {rMsg.message}')

        return True

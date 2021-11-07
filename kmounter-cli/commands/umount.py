from argparse import ArgumentParser, _SubParsersAction
from socket import socket

from google.protobuf.message import Message

from commands.common import Command
from common.actions_pb2 import ActionMessage, Umount
from common.const import MessageType
from common.packet import Packet


class UmountCommand(Command):
    @staticmethod
    def enrich_args(subParsers: _SubParsersAction) -> None:
        parser: ArgumentParser = subParsers.add_parser(
            'umount', help='Umount a previously mounted volume')
        parser.add_argument('name', help='The name given to a previously mounted volume')
        parser.add_argument(
            '--home-symlink',
            help="The symlink path relative to the user's home to unlink",
            default=False)
        parser.add_argument('--force', '-f', action='store_true', default=False,
                            help='Force the umount (might lose data)')

    def run(self, args: ArgumentParser, sock: socket) -> bool:
        arguments, _ = args.parse_known_args()

        if arguments.command != 'umount':
            return False

        msg: Message = Umount()
        msg.mount_name = arguments.name
        msg.home_sym_link = arguments.home_symlink
        msg.force = arguments.force

        packet = Packet(MessageType.UMOUNT, msg)
        sock.send(packet.serialize())
        response = Packet.read(sock)

        if response.type == MessageType.ERROR:
            rMsg: Message = ActionMessage()
            rMsg.ParseFromString(response.messageBytes)
            print(f'Umount error: {rMsg.message}')

        return True

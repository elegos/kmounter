from argparse import ArgumentParser, _SubParsersAction
from socket import socket

from commands.common import Command
from common.const import MessageType
from common.protocol_pb2 import Empty
from common.packet import Packet


class CheckDaemonStatusCommand(Command):
    @staticmethod
    def enrich_args(subParser: _SubParsersAction) -> None:
        subParser.add_parser('daemon-status', help='Check the daemon is running')

    def run(self, args: ArgumentParser, sock: socket) -> bool:
        arguments, _ = args.parse_known_args()

        if arguments.command != 'daemon-status':
            return False

        status = 'NOT RUNNING'

        try:
            packet = Packet(MessageType.PING, Empty())
            sock.send(packet.serialize())
            response = Packet.read(sock)

            if response.type == MessageType.PONG:
                status = 'RUNNING'
        finally:
            print(f'Daemon status: {status}')

        return True

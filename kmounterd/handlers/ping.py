from typing import Optional

from common.const import MessageType
from common.packet import Packet
from common.protocol_pb2 import Empty
from google.protobuf.message import Message
from utils import WhoIs

from handlers.handler import Handler


class PingHandler(Handler):
    @staticmethod
    def canHandle(messageType: MessageType) -> bool:
        return messageType == MessageType.PING

    def handle(self, who: WhoIs, message: bytes) -> Optional[Packet]:
        ping: Message = Empty()
        ping.ParseFromString(message)

        return Packet(MessageType.PONG, message=Empty())

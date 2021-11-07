from dataclasses import dataclass
from socket import socket
from typing import Optional

from google.protobuf.message import Message
from common.const import MessageType
from common.protocol_pb2 import Packet as ProtocolPacket

LEN_BYTES = 8


@dataclass
class Packet:
    type: MessageType
    message: Optional[Message] = None
    messageBytes: Optional[bytes] = None

    @staticmethod
    def _serlen(b: bytes) -> bytes:
        return len(b).to_bytes(LEN_BYTES, 'little')

    def serialize(self) -> bytes:
        req: Message = ProtocolPacket()
        req.type = self.type.value
        req = req.SerializeToString()
        msg = self.message.SerializeToString()

        return self._serlen(req) + req + self._serlen(msg) + msg

    @staticmethod
    def read(sock: socket) -> 'Packet':
        size = int.from_bytes(sock.recv(LEN_BYTES), 'little')
        msgBytes = sock.recv(size)
        protoPacket: Message = ProtocolPacket()
        protoPacket.ParseFromString(msgBytes)

        size = int.from_bytes(sock.recv(LEN_BYTES), 'little')
        msgBytes = sock.recv(size)

        return Packet(type=MessageType(protoPacket.type), messageBytes=msgBytes)

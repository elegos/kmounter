from typing import Optional
from common.packet import Packet
from handlers.handler import Handler
from utils import WhoIs
from common.const import MessageType


class MountAndSync(Handler):
    def canHandle(messageType: MessageType) -> bool:
        return messageType == MessageType.MOUNT_AND_SYNC

    def handle(who: WhoIs, message: bytes) -> Optional[Packet]:
        return super().handle(message)

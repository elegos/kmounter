from abc import ABC, abstractmethod
from typing import Optional
from common.const import MessageType

from common.packet import Packet
from utils import WhoIs


class Handler(ABC):
    @abstractmethod
    def canHandle(messageType: MessageType) -> bool:
        pass

    @abstractmethod
    def handle(who: WhoIs, message: bytes) -> Optional[Packet]:
        pass

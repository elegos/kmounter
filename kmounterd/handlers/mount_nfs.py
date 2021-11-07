import logging
from pathlib import Path
from typing import List, Optional

from common.actions_pb2 import ActionMessage, Mount, MountNFS
from common.const import MessageType
from common.packet import Packet
from common.settings import Settings
from google.protobuf.message import Message
from services import mount, symlink
from utils import WhoIs

from handlers.handler import Handler

MS_REMOUNT = 32


class MountNFSHandler(Handler):
    settings: Settings

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    @staticmethod
    def canHandle(messageType: MessageType) -> bool:
        return messageType == MessageType.MOUNT_NFS

    def handle(self, who: WhoIs, message: bytes) -> Optional[Packet]:
        msg: Message = MountNFS()
        msg.ParseFromString(message)

        try:
            mounted = mount.mountNFS(self.settings.mountPath, who, msg)
            if msg.home_sym_link:
                target = Path(msg.home_sym_link)
                source = Path(mounted.target).absolute()

                symlink.makeHomeSymlink(who, source, target)
        except Exception as e:
            logging.error(f'{who} | {e}')

            errMsg: Message = ActionMessage()
            errMsg.message = str(e)

            return Packet(MessageType.ERROR, errMsg)

        outMsg: Message = ActionMessage()
        outMsg.message = f'{msg.source} succesfully mounted on {mounted.target}'
        if mounted.remounted:
            outMsg.message += ' (remounted)'
        logging.info(f'{who} | {outMsg.message}')

        return Packet(MessageType.OK, outMsg)

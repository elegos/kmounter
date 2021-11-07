import ctypes
import logging
import os
from pathlib import Path
from typing import Optional

import netifaces
from common.actions_pb2 import ActionMessage, Umount
from common.const import MessageType
from common.packet import Packet
from common.settings import Settings
from google.protobuf.message import Message
from services import mount, symlink
from utils import WhoIs

from handlers.handler import Handler


class UmountHandler(Handler):
    settings: Settings

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    @staticmethod
    def canHandle(messageType: MessageType) -> bool:
        return messageType == MessageType.UMOUNT

    def handle(self, who: WhoIs, message: bytes) -> Optional[Packet]:
        msg: Message = Umount()
        msg.ParseFromString(message)

        mountPath = mount.getMountPath(self.settings.mountPath, who, msg.mount_name)

        try:
            mounted = mount.umount(mountPath, msg)

            if not mounted:
                outMsg: Message = ActionMessage()
                outMsg.message = f'Mount "{msg.mount_name}" was not mounted, nothing to do.'

                return Packet(MessageType.OK, outMsg)

            if msg.home_sym_link:
                target = Path(msg.home_sym_link)
                source = Path(mounted.target).absolute()

                symlink.unlink(who, source, target)
        except Exception as e:
            outMsg: Message = ActionMessage()
            outMsg.message = str(e)

            logging.debug(f'{who} | {outMsg.message}')
            return Packet(MessageType.ERROR, outMsg)

        outMsg: Message = ActionMessage()
        outMsg.message = f'{msg.mount_name} succesfully umounted'
        if msg.force:
            outMsg.message += ' (forced umount)'
        logging.debug(f'{who} | {outMsg.message}')

        return Packet(MessageType.OK, outMsg)

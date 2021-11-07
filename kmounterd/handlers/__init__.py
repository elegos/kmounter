from typing import List

from handlers.handler import Handler
from handlers.mount_nfs import MountNFSHandler
from handlers.ping import PingHandler

handlers: List[Handler] = [PingHandler, MountNFSHandler]

import logging
import os
import signal
import socket
from argparse import ArgumentParser
from threading import Thread
from typing import List, Optional

from common.packet import Packet
from common.settings import Settings
from handlers.handler import Handler
from handlers.mount_nfs import MountNFSHandler
from handlers.ping import PingHandler
from handlers.umount import UmountHandler
from sigcapture import SigCapture
from utils import whois

handlers: List[Handler] = []


def loggingSetup(settings: Settings) -> None:
    logging.basicConfig(
        format='%(asctime)-15s %(levelname)-10s %(message)s',
        level=logging.getLevelName(settings.logLevel)
    )


def setup(settings: Settings) -> socket.socket:
    global handlers
    handlers.extend([PingHandler(), MountNFSHandler(settings), UmountHandler(settings)])

    try:
        settings.socketPath.unlink(missing_ok=True)
    except OSError as e:
        logging.error(f'Failed removing previous sock file, shutting down: {e}')
        os._exit(2)

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(str(settings.socketPath.absolute()))
        os.chmod(str(settings.socketPath.absolute()), 0o777)
    except PermissionError as e:
        logging.error(f"Can't bind to {settings.socketPath.absolute()}: {e}")
        os._exit(3)

    return sock


def routine(connection: socket.socket):
    who = whois(connection)
    packet = Packet.read(connection)

    logging.debug(
        f'{who} | PID: {who} UID: {who.uid} ({who.username}) GID: {who.gid} ({who.group})')
    logging.debug(f'{who} | Received packet type: {packet.type}')

    response: Optional[Packet] = None
    handled = False
    for handler in handlers:
        if handler.canHandle(packet.type):
            response = handler.handle(who, packet.messageBytes)
            handled = True
            break

    if not handled:
        logging.warning(f'Unhandled message type: "{packet.type}"')

    if response is not None:
        connection.send(response.serialize())
        logging.debug(f'{who} | Sent packet type: {response.type}')

    connection.close()


args = ArgumentParser()
settings = Settings.fromArgs(args)

loggingSetup(settings)
sock = setup(settings)

sock.listen(1)

threadsPool: List[Thread] = []
try:
    with SigCapture(signal.SIGINT) as capt:
        while capt.isRunning:
            connection, _ = sock.accept()

            thread = Thread(target=routine, args=[connection])
            threadsPool.append(thread)
            thread.start()
except KeyboardInterrupt:
    pass

# Tear down
for thread in threadsPool:
    thread.join()

sock.close()

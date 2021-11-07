from abc import ABC, abstractmethod
from argparse import Namespace
from socket import socket

from argparse import _SubParsersAction


class Command(ABC):
    @staticmethod
    @abstractmethod
    def enrich_args(subParsers: _SubParsersAction) -> None: pass

    @abstractmethod
    def run(self, args: Namespace, sock: socket) -> bool: pass

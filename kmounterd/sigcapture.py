import logging
import signal
from threading import Event
from typing import Any


class SigCapture:
    sig: Any
    loop: Event

    def __init__(self, sig=signal.SIGINT) -> None:
        self.sig = sig
        self.loop = Event()

    def __enter__(self) -> 'SigCapture':
        self.loop.clear()
        signal.signal(self.sig, self._signal_handler)

        return self

    def __exit__(self, type, value, traceback):
        if traceback is not None and type is not KeyboardInterrupt:
            logging.error(f'{type} - {value}')
            logging.error(traceback)
        if not self.isRunning:
            self.loop.set()

    def _signal_handler(self, sig, frame):
        self.loop.set()

        raise KeyboardInterrupt()

    @property
    def isRunning(self) -> bool:
        return not self.loop.is_set()

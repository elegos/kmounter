import ctypes
import os
from typing import Optional


LIBC = ctypes.CDLL('libc.so.6', use_errno=True)


def analyzeExitCode(exitCode: int, procedure: str) -> Optional[str]:
    ''' Returns an eventual error message '''
    if exitCode != 0:
        errno = ctypes.get_errno()
        errmsg = os.strerror(errno)

        return f'An error occurred during the {procedure} procedure (return value: {exitCode}, errno: {errno} - {errmsg})'

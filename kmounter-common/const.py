from enum import Enum


class MessageType(Enum):
    PING = 'Ping'
    PONG = 'Pong'

    # Mount only
    UMOUNT = 'Umount'
    MOUNT_NFS = 'MountNFS'

    # Sync
    MOUNT_AND_SYNC = 'MountAndSync'
    UMOUNT_AND_STOP_SYNC = 'UmountAndStopSync'

    # Responses
    OK = 'OK'
    ERROR = 'Error'

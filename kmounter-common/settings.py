import logging
from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
from typing import Optional


class Settings:
    args: ArgumentParser
    socketPath: Path
    mountPath: Path
    logLevel: str

    def __init__(self,
                 args: ArgumentParser,
                 logLevel: str = 'INFO',
                 confPath: Optional[Path] = None,
                 sockPath: Optional[Path] = None):
        self.args = args

        if confPath is None and sockPath is None:
            confPath = Settings.locateConfigPath()

        logging.getLogger().setLevel(logging.getLevelName(logLevel))

        error: Optional[str] = None
        if confPath is not None and not confPath.is_file():
            error = f'Config file: not found ({confPath.absolute()})'
        if sockPath is not None and not sockPath.exists():
            error = f'Socket file: not found ({sockPath.absolute()})'

        if error is not None:
            raise Exception(error)

        config = ConfigParser()
        if confPath is not None:
            config.read(str(confPath.absolute()))

        self.socketPath = sockPath if sockPath is not None else Path(
            config.get('paths', 'socket', fallback=str(sockPath)))
        self.mountPath = Path(config.get('paths', 'mount_prefix', fallback='/run/media'))

        if confPath is not None:
            if not self.socketPath.is_absolute():
                self.socketPath = confPath.parent.absolute().joinpath(self.socketPath)
            if not self.mountPath.is_absolute():
                self.mountPath = confPath.parent.absolute().joinpath(self.mountPath)

        self.logLevel = config.get('kmounterd', 'log_level', fallback='WARN')

    @staticmethod
    def locateConfigPath() -> Optional[Path]:
        orderedPaths = [Path().cwd(), Path('/usr/local/etc'), Path('/etc')]

        for path in orderedPaths:
            confPath = path.joinpath('kmounterd.conf')
            if confPath.is_file():
                return confPath

        logging.error(
            f"Can't find configuration file in [{', '.join([str(p) for p in orderedPaths])}]")

        return None

    @staticmethod
    def fromArgs(argsParser: ArgumentParser) -> 'Settings':
        argsParser.add_argument('--config-path', '-c', required=False,
                                help='Path to the configuration file')
        argsParser.add_argument('--socket-path', '-s', required=False,
                                help='Path to the unix socket')
        argsParser.add_argument('--debug', '-d', required=False, action='store_true',
                                help='Enable debug output')

        args = argsParser.parse_known_args()[0]

        kwargs = {}
        kwargs['confPath'] = Path(args.config_path) if args.config_path is not None else None
        kwargs['sockPath'] = Path(args.socket_path) if args.socket_path is not None else None
        kwargs['logLevel'] = 'DEBUG' if args.debug else None

        for key, value in list(kwargs.items()):
            if value is None:
                del(kwargs[key])

        return Settings(args=argsParser, **kwargs)

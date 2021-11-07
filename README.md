# Kmounter

![Programming language: Python](https://img.shields.io/badge/language-python-97c510)
![Python minimum version: 3.10](https://img.shields.io/badge/python%20version-3.10-97c510)

[![License: GNU GPLv3](https://img.shields.io/badge/license-GPLv3-97c510)](LICENSE)

This project aims to create a daemon-client application able to mount and umount volumes in the user-space, without the need of administrative privileges.

The focus of the project is to be able to mount NFS partitions and create a simple backup functionality, using kernel's `inotify` or relying on a 3rd party utility (rsync for instance).

The programming language used is Python, libc is used for advanced mount operations via ctypes and protobuf is used as message data structure.

This software is released under the GNU GPL v3. A copy of the license can be found in the [LICENSE](LICENSE) file.

## Project dependencies:

- System dependencies:
    - libc.so.6
- Python libraries (entire echosystem):
    - protobuf
    - netifaces

## Install

The project is still a work-in-progress. Installation process will follow.

## Project ecosystem

### kmounterd

Daemon which runs with root privileges, listening on a UNIX socket. It allows users to mount and monitor only paths within the user's space (HOME directory), mounting target volumes in `/run/media/$USER` (with the option to symlink in the user's home). Default socket position is `/var/run/kmounterd.sock`. The root privileges are required to call the system's mount operations.

Run `kmounterd --help` for a list of run options

### kmounter-cli

Client's command line interface of kmounterd. Allows to operate all the functionalities of the daemon.

Run `kmounter-cli --help` for a list of options. Subcommand help information is accessible via `kmounter-cli <command> --help`

### kmounter-gui

Client's graphical interface, thought to be implemented with Qt libraries. Not implemented yet.

### kmounter-common

Common library between daemon and client(s), storing `*.proto` files, derived `*_pb2.py` files, constants (like message types) etc.

## Supported operations:

- Mount NFS (versions 4.2, 4.1)
- Symlink mounts in user's HOME
- Unmount mounted partitions, with eventual unlink of symlinks (can only unlink symlinks pointing to the user's mounts)

## Prioritized to-be:

- Mount for backup (rsync?)
- Other network filesystems (Samba?)

## Contribute

### New actions

This project takes advantage of `pipenv`: if you want to use it, just install the dev dependencies via `pipenv install -d` and then use its virtual environment via `pipenv`subcommands (i.e. `pipenv run python main.py`). Otherwise read the `Pipfile` file and install the dependencies manually (it is highly suggested to use `pipenv`).

All the actions start with the following elements:

- A message in `kmounter-common/proto-messages/actions.proto`, then generated via `cd kmounter-common && ./make build`
- A new message type in `kmounter-common/const.py`
- A handler class in `kmounterd/handlers`, extending `handlers.handler.Handler`, wired into `kmounterd/main.py`
- A command in `kmounter-cli/commands`, extending `commands.common.Command`, wired into `kmounter-cli/main.py`
- (TODO) GUI integration

Working on the daemon, please be very careful about possible security expolits: always ensure that the user is allowed to perform the required actions. The `WhoIs` object helps identifying the user connected to the socket.

Use `logging.[error|warning|info|debug]` instead of print, and always format the message as follows: `f'{who} | message'`, where `who` is the `WhoIs` message.

Within the daemon, exceptions are designed to pop inside the handlers, not outside of them. Please `try...except` them within the handlers. The same applies to the CLI's commands.

Please be compliant with the pep8 (99 columns per line) standard (or just run autopep8).

Note that most of the actions run by the daemon require root privileges. In order to test it, it is suggested to run it via `sudo`, or as root (at your own risk).

import os
from enum import Enum
from typing import NoReturn

from .connection import Connection
from .shell import parse_mode


class ActionMode(Enum):
    NO_CLOSE = 1
    NO_RENAME = 2


def parse_mode_env(action: ActionMode) -> bool:
    match action:
        case ActionMode.NO_CLOSE:
            return bool(parse_mode().R or os.environ.get("SSH_M_R"))
        case ActionMode.NO_RENAME:
            return bool(parse_mode().C or os.environ.get("SSH_M_C"))
    return False


def run_in_tmux(connection: Connection) -> NoReturn:
    """Run SSH connection with specified TMUX features
    Could rename an active window to user@hostname and terminates window on connection close

    :param connection: `Connection` to be used in SSH session
    """
    if not parse_mode_env(ActionMode.NO_RENAME):
        os.system(f"tmux rename-window '{connection.remote_user}@{connection.hostname}'")
    os.system(connection.sshpass())
    if not parse_mode_env(ActionMode.NO_CLOSE):
        os.system("kill -9 %d" % (os.getppid()))  # Dirty hack from Foo Bah to close tty after ssh ends

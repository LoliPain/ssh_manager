import argparse
import os

from simple_term_menu import TerminalMenu

from .connection import Connection
from .stored import proceed_stored


def one_time_selection() -> Connection:
    store = proceed_stored()
    return store[TerminalMenu([str(_) for _ in store]).show()]


def new_stored_entry() -> Connection:
    return Connection(
        hostname=input("Hostname (eg. google.com): "),
        remote_user=input("Remote user: "),
        named_passwd=input("Name of remote using for stored password (and env variable): "),
    )


def parse_mode() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        default=False,
        action='store_true'
    )
    return parser.parse_args()


def open_ssh():
    connection = one_time_selection()
    if os.environ.get("TMUX"):
        os.system(f"tmux rename-window '{connection.remote_user}@{connection.hostname}'")
    os.system(connection.sshpass())
    if os.environ.get("TMUX"):
        os.system("kill -9 %d" % (os.getppid()))  # Dirty hack from Foo Bah to close tty after ssh ends

from simple_term_menu import TerminalMenu
import argparse
from stored import proceed_stored
from connection import Connection


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

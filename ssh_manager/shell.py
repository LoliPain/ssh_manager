import os
import sys

from InquirerPy import inquirer, get_style
from InquirerPy.base.control import Choice
from InquirerPy.enum import INQUIRERPY_POINTER_SEQUENCE as pointer_code

from .connection import Connection
from .stored import proceed_stored
from .tmux import run_in_tmux


def one_time_selection() -> Connection:
    """Start an interactive selection

    :return: Selected connection instance
    """
    store = proceed_stored()
    selected = inquirer.select(
        message="Select SSH user:",
        qmark="",
        amark=pointer_code,
        cycle=True,
        vi_mode=True,
        mandatory=False,
        show_cursor=False,
        raise_keyboard_interrupt=False,
        long_instruction="exit: C-c, q",
        keybindings={"skip": [{"key": "q"}, {"key": "c-c"}]},
        choices=[Choice(value=i, name=str(_)) for i, _ in enumerate(store)],
        style=get_style({"answermark": "#61afef"}, style_override=False)
    ).execute()
    if selected is None:
        sys.exit(0)  # Exit on 'q' press
    return store[selected]


def new_stored_entry() -> Connection:
    """Step-by-step creating new stored info

    :return: Recently created connection instance
    """
    return Connection(
        hostname=input("Hostname (eg. google.com): "),
        remote_user=input("Remote user: "),
        named_passwd=input("Name of remote using for stored password (and env variable): "),
    )


def open_ssh() -> None:
    """Start an SSH connection
    Checks whenever runs inside TMUX session, then proceeds further handling in `run_in_tmux`

    :return: No.
    """
    connection = one_time_selection()
    if os.environ.get(connection.env_passwd()):
        if os.environ.get("TMUX"):
            run_in_tmux(connection)
        else:
            os.system(connection.sshpass())
    else:
        print(f"${connection.env_passwd()} is empty!")

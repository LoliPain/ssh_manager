import os
import sys
from typing import Optional

from InquirerPy import inquirer, get_style
from InquirerPy.enum import INQUIRERPY_POINTER_SEQUENCE as pointer_code
from InquirerPy.base.control import Choice

from .connection import Connection
from .stored import proceed_stored, append_to_stored
from .tmux import run_in_tmux


def one_time_selection() -> Optional[Connection]:
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
        long_instruction="new: n, delete: d\nexit: C-c, q",
        keybindings={"skip": [{"key": "q"}, {"key": "c-c"}]},
        choices=[Choice(value=i, name=str(_)) for i, _ in enumerate(store)],
        style=get_style({"answermark": "#61afef"}, style_override=False)
    )

    @selected.register_kb('d')
    def _delete_entry(ctx):
        ctx.app.exit(result='del')

    @selected.register_kb('n')
    def _new_entry(ctx):
        ctx.app.exit(result='new')

    selected = selected.execute()
    match selected:
        case 'new':
            return append_to_stored(new_stored_entry())
        case 'del':
            ...
        case None:
            sys.exit(0)  # Exit on 'skip' action
        case _:
            return store[selected]


def new_stored_entry() -> Connection:
    """Step-by-step creating new stored info

    :return: Recently created connection instance
    """
    def inquirer_wrapper_input(message: str, **kwargs):
        """Pre-configured :inquirer.text with provided placeholder
        Additional arguments would be passed as kwargs

        :return: Answer to text input
        """
        return inquirer.text(
            message=message,
            mandatory=True,
            amark=pointer_code,
            validate=lambda self: len(self) > 0,
            long_instruction="exit: C-c",
            **kwargs
        ).execute()
    return Connection(
        hostname=inquirer_wrapper_input("Hostname", instruction="(eg. google.com):"),
        remote_user=inquirer_wrapper_input("Remote user:"),
        named_passwd=inquirer_wrapper_input("Environment variable suffix", instruction="(eg. server in server_user):"),
    )


def open_ssh() -> None:
    """Start an SSH connection
    Checks whenever runs inside TMUX session, then proceeds further handling in `run_in_tmux`

    :return: No.
    """
    connection = one_time_selection()
    if not connection:
        open_ssh()
    if os.environ.get(connection.env_passwd()):
        if os.environ.get("TMUX"):
            run_in_tmux(connection)
        else:
            os.system(connection.sshpass())
    else:
        print(f"${connection.env_passwd()} is empty!")

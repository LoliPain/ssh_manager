import os.path
from json import load
from typing import List, Union

from colorama import Back, Fore, Style
from pydantic import TypeAdapter, ValidationError

from .store_path import store_path
from ..connection import Connection, StoredConnection


def read_whole_store() -> List[StoredConnection]:
    """Get all stored entries as plain dicts

    :return: Storage object or [] if not exist
    """
    if os.path.exists(store_path):
        with open(store_path, 'r') as f:
            stored_connections = TypeAdapter(List[StoredConnection])
            try:
                loaded = stored_connections.validate_python(load(f))
            except ValidationError as e:
                import builtins
                exception_header = (
                    f"{Style.RESET_ALL + Fore.RED + store_path + Style.RESET_ALL}\n"
                    f"Storage entries contains: {Back.RED + Fore.WHITE}{e.error_count()} validation errors "
                    f"{Style.RESET_ALL}\n"
                )
                for _ in e.errors():
                    exception_header += (
                        f"\n\n{Fore.RED + _['msg'] + Style.RESET_ALL} "
                        f"{Back.RED + _['loc'][1] + Style.RESET_ALL} where is:\n\n"
                    )
                    match type(_['input']):
                        case builtins.dict:
                            exception_header += "\n".join(
                                [f'{Fore.CYAN + z + Style.RESET_ALL}: ({y})' for z, y in _['input'].items()]
                            )
                        case _:
                            exception_header += (
                                f"{Fore.CYAN} {_['input']} {Style.RESET_ALL}"
                            )
                raise SystemExit(exception_header)
        return loaded
    return []


def proceed_stored() -> Union[list, List[Connection]]:
    """Automatically read all stored entries and proceed it to `Connection` instances

    :return: List of all stored entries
    """
    stored = []
    loaded = read_whole_store()
    for i in loaded:
        stored.append(
            Connection(
                hostname=i.hostname,
                remote_user=i.remote_user,
                named_passwd=i.named_passwd
            )
        )

    return stored

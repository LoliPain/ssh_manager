import os.path
from json import load
from typing import List, Union

from .store_path import store_path
from ..connection import Connection


def read_whole_store() -> Union[list, List[dict]]:
    """Get all stored entries as plain dicts

    :return: Storage object or [] if not exist
    """
    if os.path.exists(store_path):
        with open(store_path, 'r') as f:
            loaded: List[dict] = load(f)
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
                hostname=i.get("hostname"),
                remote_user=i.get("remote_user"),
                named_passwd=i.get("named_passwd")
            )
        )

    return stored

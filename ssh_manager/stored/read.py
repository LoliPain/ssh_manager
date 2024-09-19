import os.path
from json import load
from typing import List, Union

from pydantic import TypeAdapter
from typing_extensions import Never

from .store_path import store_path
from ..connection import Connection, StoredElement


def read_whole_store() -> Union[List[Never], List[StoredElement]]:
    """Get all stored entries as plain dicts

    :return: Storage object or [] if not exist
    """
    if os.path.exists(store_path):
        with open(store_path, 'r') as f:
            stored_elements = TypeAdapter(List[StoredElement])
            loaded = stored_elements.validate_python(load(f))
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

import os.path
from json import load
from typing import List

from .store_path import store_path
from ..connection import Connection


def read_whole_store() -> list:
    if os.path.exists(store_path):
        with open(store_path, 'r') as f:
            loaded: List[dict] = load(f)
        return loaded
    return []


def proceed_stored() -> list:
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

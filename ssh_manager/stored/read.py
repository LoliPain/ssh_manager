from json import load
from typing import List

from ..connection import Connection


def read_whole_store() -> list:
    with open('stored/cx.json', 'r') as f:
        loaded: List[dict] = load(f)
    return loaded


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

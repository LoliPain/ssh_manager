from json import dumps

from .read import read_whole_store
from .store_path import store_path
from ..connection import Connection


def append_to_stored(connection: Connection):
    loaded = read_whole_store()
    with open(store_path, 'w+') as f:
        loaded.append(connection.to_json())
        f.write(dumps(loaded))
    return

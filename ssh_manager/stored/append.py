from json import dumps

from .read import read_whole_store
from .store_path import store_path
from ..connection import Connection


def append_to_stored(connection: Connection):
    """Add new connection to storage
    If storage file not exists creates it

    :param connection: Freshly created connection
    :return: No.
    """
    loaded = read_whole_store()
    with open(store_path, 'w+') as f:
        loaded.append(connection.to_json())
        f.write(dumps(loaded))
    return

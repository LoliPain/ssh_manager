from connection import Connection
from json import dumps
from .read import read_whole_store


def append_to_stored(connection: Connection):
    loaded = read_whole_store()
    with open('stored/cx.json', 'w') as f:
        loaded.append(connection.to_json())
        f.write(dumps(loaded))
    return

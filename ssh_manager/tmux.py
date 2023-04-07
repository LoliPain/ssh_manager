import os
from typing import Callable

from ssh_manager.connection import Connection


def run_in_tmux(connection: Connection):
    os.system(f"tmux rename-window '{connection.remote_user}@{connection.hostname}'")
    os.system(connection.sshpass())
    os.system("kill -9 %d" % (os.getppid()))  # Dirty hack from Foo Bah to close tty after ssh ends

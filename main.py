import os

from cli import parse_mode, new_stored_entry, one_time_selection
from stored import append_to_stored


def invoke_cmd():
    connection = one_time_selection()
    if os.environ.get("TMUX"):
        os.system(f"tmux rename-window '{connection.remote_user}@{connection.hostname}'")
    os.system(connection.sshpass())
    if os.environ.get("TMUX"):
        os.system("kill -9 %d" % (os.getppid()))  # Dirty hack from Foo Bah to close tty after ssh ends


def routing(is_new: bool):
    if is_new:
        append_to_stored(new_stored_entry())
    invoke_cmd()


if __name__ == "__main__":
    print("ssh_manager: \n")
    routing(parse_mode().n)

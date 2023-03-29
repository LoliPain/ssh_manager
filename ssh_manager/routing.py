from .shell import new_stored_entry, open_ssh
from .stored import append_to_stored


def routing(is_new: bool):
    if is_new:
        append_to_stored(new_stored_entry())
    open_ssh()

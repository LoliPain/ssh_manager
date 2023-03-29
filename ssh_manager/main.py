from .routing import routing
from .shell import parse_mode


def main():
    """Entrypoint for `setup.py`

    :return: No, lol.
    """
    print("ssh_manager: \n")
    routing(parse_mode().n)


if __name__ == "__main__":
    main()

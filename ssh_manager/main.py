from .parse_args import parse_mode
from .routing import routing


def main():
    """Entrypoint for `setup.py`

    :return: No, lol.
    """
    print("ssh_manager: \n")
    routing(parse_mode().n)


if __name__ == "__main__":
    main()

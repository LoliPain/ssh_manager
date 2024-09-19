from .parse_args import parse_mode
from .routing import routing


def main():
    """Entrypoint for `setup.py`

    :return: No, lol.
    """
    routing(parse_mode().n)


if __name__ == "__main__":
    main()

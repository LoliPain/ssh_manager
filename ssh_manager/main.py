from .parse_args import parse_mode
from .routing import routing


def main():
    """Entrypoint for `setup.py`

    :return: No, lol.
    """
    print("ssh_manager: \n")
    try:
        routing(parse_mode().n)
    except KeyboardInterrupt:
        raise SystemExit('\n')


if __name__ == "__main__":
    main()

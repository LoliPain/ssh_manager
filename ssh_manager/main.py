from pkg_resources import get_distribution

from .parse_args import parse_mode
from .routing import routing


def main():
    """Entrypoint for `setup.py`

    :return: No, lol.
    """
    print(f"ssh_manager v{get_distribution('ssh_manager').version}: \n")
    routing(parse_mode().n)


if __name__ == "__main__":
    main()

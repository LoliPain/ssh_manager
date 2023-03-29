from .shell import parse_mode
from .routing import routing


def main():
    print("ssh_manager: \n")
    routing(parse_mode().n)


if __name__ == "__main__":
    main()

from .routing import routing
from .shell import parse_mode


def main():
    print("ssh_manager: \n")
    routing(parse_mode().n)


if __name__ == "__main__":
    main()

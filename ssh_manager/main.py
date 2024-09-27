from importlib.metadata import version
from os import environ

from .runtime_exceptions import StorageProcessingError
from .exception_handlers import handle_gracefully, format_exception
from .parse_args import parse_mode
from .routing import routing


def main():
    """Entrypoint for `setup.py`

    :return: No, lol.
    """
    print(f"ssh_manager "
          f"v{version('ssh_m.py') if not environ.get('SSH_M_PREVIEW_MODE') else '0.x.y'}:\n"
          )
    try:
        routing(parse_mode().n)
    except (KeyboardInterrupt,
            StorageProcessingError) as e:
        handle_gracefully(e)
    except Exception as e:
        raise format_exception(e)


if __name__ == "__main__":
    main()

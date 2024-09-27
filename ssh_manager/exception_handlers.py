from .runtime_exceptions import StorageProcessingError
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText


def handle_gracefully(e):
    if isinstance(e, StorageProcessingError):
        formatted_text = [("", e.ctx or "")]
        if type(e.accent) is str:
            formatted_text += [("", "\n"), ("#ff0000 underline", e.accent)]
        print_formatted_text(FormattedText(formatted_text))
    elif isinstance(e, KeyboardInterrupt):
        ...
    print("\n")
    raise SystemExit


def format_exception(e) -> type[Exception]:
    return e

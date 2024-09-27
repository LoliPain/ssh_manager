from json import JSONDecodeError

from .runtime_exceptions import StorageProcessingError
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from pydantic_core import ValidationError


def handle_gracefully(e):
    formatted_text = []
    if isinstance(e, StorageProcessingError):
        formatted_text = [("", e.ctx or "")]
        if type(e.accent) is str:
            formatted_text += [("", "\n"), ("#ff0000 underline", e.accent)]
    elif isinstance(e, JSONDecodeError):
        formatted_text = [("", f"JSON decoding error at line {e.lineno} col {e.colno}"),
                          ("", "\n"), ("#ff0000 underline", e.msg)]
    elif isinstance(e, ValidationError):
        ...

    formatted_text += [("", "\n\n"), ("#abb2bf", "Most likely this was caused by fact that you edited the storage")]
    print_formatted_text(FormattedText(formatted_text))
    raise SystemExit


def format_exception(e) -> type[Exception]:
    return e

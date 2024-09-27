from typing import Any


class RuntimeProcessingError(Exception):
    """Exception should be raised when normally impossible things are happen
    Receives multiple arguments to be shown, each starting with newline
    Normally should be never occurred during usage

    Ends with link to GitHub Issues
    """
    def __init__(self, ctx: str, *args_ctx: Any):
        self.ctx = ctx
        for aux_ctx in args_ctx:
            self.ctx += f"\n{aux_ctx}"
        self.ctx += ("\n\nThis error should be normally never occurred.\n"
                     "Please open a new ticket on Github Issues with steps to reproduce and trace above\n"
                     "https://github.com/LoliPain/ssh_manager/issues/new?assignees=&labels=invalid&projects=&template"
                     "=report-an-invalid-or-unexpected-behavior.md&title=")
        super().__init__(self.ctx)

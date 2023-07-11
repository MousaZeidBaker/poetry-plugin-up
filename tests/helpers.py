from typing import Any

from cleo.io.outputs.output import Verbosity
from poetry.console.application import Application
from poetry.poetry import Poetry
from poetry_plugin_up.command import UpCommand


class TestUpCommand(UpCommand):
    def __init__(self, poetry: Poetry):
        super().__init__()
        self._poetry = poetry

    __test__ = False

    def line(
        self,
        text: Any,
        style: str | None = None,
        verbosity: Verbosity | None = None,
    ):
        print(text)


class TestApplication(Application):
    def __init__(self, poetry: Poetry):
        super().__init__()
        self._poetry = poetry

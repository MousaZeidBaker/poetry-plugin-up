from typing import Any

import pytest
from poetry.console.application import Application
from poetry.poetry import Poetry

from poetry_plugin_up.command import UpCommand
from src.poetry_plugin_up.command import poetry_version_above_2

poetry_v1 = pytest.mark.skipif(
    poetry_version_above_2(),
    reason="Requires Poetry below 2.0.0.",
)

poetry_v2 = pytest.mark.skipif(
    not poetry_version_above_2(),
    reason="Requires Poetry 2.0.0 or up.",
)


class TestUpCommand(UpCommand):
    def __init__(self, poetry: Poetry) -> None:
        super().__init__()
        self._poetry = poetry

    __test__ = False

    def line(self, data: Any):
        print(data)


class TestApplication(Application):
    def __init__(self, poetry: Poetry) -> None:
        super().__init__()
        self._poetry = poetry

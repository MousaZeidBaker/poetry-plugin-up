from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_up.command import UpCommand

if TYPE_CHECKING:
    from poetry.console.application import Application


def factory() -> UpCommand:
    return UpCommand()


class UpApplicationPlugin(ApplicationPlugin):
    def activate(self, application: Application):
        application.command_loader.register_factory("up", factory)

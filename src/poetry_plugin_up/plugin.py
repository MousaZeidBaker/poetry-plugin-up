from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_up.command import UpCommand


def factory():
    return UpCommand()


class UpApplicationPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("up", factory)

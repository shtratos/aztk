from aztk.plugins import PluginDefinition
from aztk.error import InvalidPluginDefinition


class Plugin:
    def __init__(self, path: str, module):
        """
        Internal container for a plugin.
        :param path: Location of the plugin
        """
        self.path = path
        self.module = module
        self.definition = module.definition()
        if isinstance(self.definition, PluginDefinition):
            raise InvalidPluginDefinition(
                "Plugin {0} definition method doesn't return a PluginDefinition object".
                format(path))
        self.name = self.definition.name

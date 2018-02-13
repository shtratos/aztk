import os
import importlib.util
from .plugin import Plugin
from aztk.models.plugins import PluginDefinition
from aztk.utils import constants
from aztk.error import InvalidPluginDefinitionError


class PluginManager:
    PluginEntryPoint = "main.py"

    def __init__(self):
        self.plugins = dict()
        self.loaded = False

    def load(self):
        if self.loaded:
            return
        self.load_all_plugins(os.path.join(constants.ROOT_PATH, "base_plugins"))
        self.loaded = True

    def has_plugin(self, name: str):
        return name in self.plugins

    def get_plugin(self, name: str):
        return self.plugins.get(name)

    def load_plugin(self, path: str):
        """
        Load a plugin at the given path
        """
        path = os.path.abspath(path)
        plugin_module = self._load_plugin_module(path)
        plugin = Plugin(path, plugin_module)

        self.plugins[plugin.name] = plugin

    def load_all_plugins(self, directory: str):
        for folder in os.listdir(directory):
            self.load_plugin(os.path.join(directory, folder))

    def _load_plugin_module(self, path: str):
        entry_file = self._get_entry_point(path)
        spec = importlib.util.spec_from_file_location("main", entry_file)
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        self._validate_plugin_module(path, plugin_module)
        return plugin_module

    def _get_entry_point(self, path: str):
        if not os.path.exists(path):
            raise InvalidPluginDefinitionError("Plugin cannot be loaded. Path '{0}' doesn't exists.".format(path))
        entry = os.path.join(path, PluginManager.PluginEntryPoint)
        if not os.path.exists(entry):
            raise InvalidPluginDefinitionError(
                "Plugin cannot be loaded. Path '{0}' doesn't contain an entry file {1}.".format(
                    path, PluginManager.PluginEntryPoint))

        return entry

    def _validate_plugin_module(self, path, plugin_module):
        if not hasattr(plugin_module, "definition"):
            raise InvalidPluginDefinitionError(
                "Plugin cannot be loaded. Plugin '{0}' is missing a function called 'definition'".format(path))

    def _expand_definition(self, path: str, definition: PluginDefinition):
        """

        """
        new_files = []
        for file in definition.files:
            new_files.append(os.path.join(path, file))
        definition.files = new_files

        return definition


plugin_manager = PluginManager()
plugin_manager.load()

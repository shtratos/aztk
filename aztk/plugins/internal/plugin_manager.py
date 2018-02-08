import os
from aztk import error
import importlib.util


class PluginManager:
    PluginEntryPoint = "main.py"

    def __init__(self):
        self.plugins = []

    def load_plugin(self, path: str):
        """
        Load a plugin at the given path
        """
        plugin_module = self._load_plugin_module(path)
        manifest = plugin_module.manifest()
        print("Entry", manifest.name)

    def _load_plugin_module(self, path: str):
        entry_file = self._get_entry_point(path)
        spec = importlib.util.spec_from_file_location("main", entry_file)
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        self._validate_plugin_module(path, plugin_module)
        return plugin_module

    def _get_entry_point(self, path: str):
        if not os.path.exists(path):
            raise error.InvalidPluginDefinition("Plugin cannot be loaded. Path '{0}' doesn't exists.".format(path))
        entry = os.path.join(path, PluginManager.PluginEntryPoint)
        if not os.path.exists(entry):
            raise error.InvalidPluginDefinition(
                "Plugin cannot be loaded. Path '{0}' doesn't contain an entry file {1}.".format(path, PluginManager.PluginEntryPoint))

        return os.path.abspath(entry)

    def _validate_plugin_module(self, path, plugin_module):
        if not hasattr(plugin_module, "manifest"):
            raise error.InvalidPluginDefinition(
                "Plugin cannot be loaded. Plugin '{0}' is missing a manifest function".format(path))

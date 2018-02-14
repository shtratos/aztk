import os
import pytest
from aztk.models.plugins.internal import PluginManager
from aztk.error import InvalidPluginDefinitionError

dir_path = os.path.dirname(os.path.realpath(__file__))
fake_plugin_dir = os.path.join(dir_path, "fake_plugins")

def test_invalid_path():
    plugin_manager = PluginManager()
    message = "Plugin cannot be loaded\. Path .* doesn't exists\."
    with pytest.raises(InvalidPluginDefinitionError, match=message):
        plugin_manager.load_plugin("/invalid/path/for/plugin/doesnot/exists")

def test_missing_main():
    plugin_manager = PluginManager()
    message = "Plugin cannot be loaded. Path .* doesn't contain an entry file main.py"
    with pytest.raises(InvalidPluginDefinitionError, match=message):
        plugin_manager.load_plugin(os.path.join(fake_plugin_dir, "missing_main"))

def test_missing_definition():
    plugin_manager = PluginManager()
    message = "Plugin .* is missing a function called 'definition'"
    with pytest.raises(InvalidPluginDefinitionError, match=message):
        plugin_manager.load_plugin(os.path.join(fake_plugin_dir, "missing_definition"))

def test_invalid_definition_returned():
    plugin_manager = PluginManager()
    message = "Plugin .* definition method doesn't return a PluginDefinition object"
    with pytest.raises(InvalidPluginDefinitionError, match=message):
        plugin_manager.load_plugin(os.path.join(fake_plugin_dir, "invalid_definition"))

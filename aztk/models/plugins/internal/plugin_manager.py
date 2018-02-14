import os
import inspect
import importlib.util
from aztk.utils import constants
from aztk.error import InvalidPluginReferenceError
from aztk.spark.models import plugins


class PluginArgument:
    def __init__(self, name: str, required: bool, default=None):
        self.name = name
        self.required = required
        self.default = default


class PluginManager:
    # Indexing of all the predefined plugins
    plugins = dict(
        jupyter=plugins.JupyterPlugin,
        rstudio_server=plugins.RStudioServerPlugin,
        hdfs=plugins.HDFSPlugin,
    )

    def __init__(self):
        self.loaded = False

    def has_plugin(self, name: str):
        return name in self.plugins

    def get_plugin(self, name: str, args: dict = None):
        if not self.has_plugin(name):
            raise InvalidPluginReferenceError("Cannot find a plugin with name '{0}'".format(self.name))

        cls = self.plugins[name]
        cls.__code__

    def get_args_for(self, cls):
        signature = inspect.signature(cls)
        args = dict()

        for k, v in signature.parameters.items():
            args[k] = PluginArgument(k, default=v.default, required=v.default is inspect.Parameter.empty)

        return args


plugin_manager = PluginManager()

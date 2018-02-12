from typing import List, Union
from enum import Enum


class PluginPort:
    """
        Definition for a port that should be opened on node
        :param internal: Port on the node
        :param public: [Optional] Port available to the user. If none won't open any port to the user
        :param name: [Optional] name to differentiate ports if you have multiple
    """

    def __init__(self, internal: int, public: Union[int,bool] = False, name=None):

        self.internal = internal
        self.expose_publicly = bool(public)
        self.public_port = None
        if self.expose_publicly:
            if public is True:
                self.public_port = internal
            else:
                self.public_port = public

        self.name = name


class PluginRunTarget(Enum):
    Master = "master"
    Worker = "worker"
    All = "all-nodes"


class PluginArgument:
    def __init__(self, name, default=None, required=None):
        if isinstance(name, str):
            self.name = name
            self.default = default
            self.required = not default if required is None else required
        elif isinstance(name, tuple):
            x, y = name
            self.name = x
            self.default = y
            self.required = len(name) == 1


class PluginDefinition:
    """
    Plugin manifest that should be returned in the main.py of your plugin
    :param name: Name of the plugin. Used to reference the plugin
    :param runOn: Where the plugin should run
    :param files: List of files to upload
    :param
    """

    def __init__(self,
                 name: str,
                 ports: List[PluginPort] = None,
                 files: List[str] = None,
                 execute: str = None,
                 args = None,
                 run_on: PluginRunTarget = PluginRunTarget.Master):
        self.name = name
        # self.docker_image = docker_image
        self.run_on = run_on
        self.ports = ports or []
        self.files = files or []
        args = args or []
        self.args = [PluginArgument(x) for x in args]
        self.execute = execute

    def has_arg(self, name: str):
        for x in self.args:
            if x.name == name:
                return True
        else:
            return False

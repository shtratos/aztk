from typing import List
from enum import Enum


class PluginPort:
    """
        Definition for a port that should be opened on node
        :param remote: Port on the node
        :param local: Port available to the user
    """

    def __init__(
            self,
            remote: int,
            local: int):

        self.remote = remote
        self.local = local


class PluginRunTarget(Enum):
    Master = "master"
    Worker = "worker"
    All = "all-nodes"


class PluginDefinition:
    """
    Plugin manifest that should be returned in the main.py of your plugin
    :param name: Name of the plugin. Used to reference the plugin
    :param runOn: Where the plugin should run
    :param files: List of files to upload
    :param
    """

    def __init__(
            self,
            name: str,
            ports: List[PluginPort] = None,
            files: List[str] = None,
            execute: str = None,
            runOn: PluginRunTarget = PluginRunTarget.Master):
        self.name = name
        # self.docker_image = docker_image
        self.runOn = runOn
        self.ports = ports or []
        self.files = files or []
        self.execute = execute

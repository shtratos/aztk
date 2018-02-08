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
    Master = 0,
    Worker = 1,
    All = 2,


class PluginDefinition:
    """
    Plugin manifest that should be returned in the main.py of your plugin
    """

    def __init__(
            self,
            name: str,
            ports: List[PluginPort] = None,
            scripts: List[str] = None,
            runOn: PluginRunTarget = PluginRunTarget.Master,
            docker_image: str = None):
        self.name = name
        self.docker_image = docker_image
        self.ports = ports or []
        self.scripts = scripts or []

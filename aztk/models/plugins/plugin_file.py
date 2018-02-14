import io
from typing import Union

class PluginFile:
    """
    Reference to a file for a plugin.
    """
    def __init__(self, target: str, content: Union[str,io.StringIO]):
        self.target = target
        if isinstance(content, str):
            self.content = content
        else:
            self.content = content.getValue()
        # TODO handle folders?

    @classmethod
    def from_local(cls, local_path: str, remote_path: str):
        with open(local_path, "r") as f:
            return cls(remote_path, f.read())

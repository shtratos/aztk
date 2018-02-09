from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget
from aztk.error import InvalidPluginConfigurationError

def definition():
    return PluginDefinition(
        name="rstudio_server",
        ports=[
            PluginPort(
                remote=8787,
                local=8787,
            ),
        ],
        runOn=PluginRunTarget.Master,
        execute="rstudio_server.sh",
        files=[
            "rstudio_server.sh",
        ],
        args=[
            "version",
        ],
    )


def validate_args(version: str = "1.1.383"):
    if version == "1.2.3":
        raise InvalidPluginConfigurationError("RStudio version is invalid")
    return True

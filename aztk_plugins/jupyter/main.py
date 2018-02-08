from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget


def definition():
    return PluginDefinition(
        name="jupyter",
        ports=[
            PluginPort(
             remote=8888,
                local=8888,
            )
        ],
        runOn=PluginRunTarget.All,
        execute="jupyter.sh",
        files=[
            "jupyter.sh",
        ],
    )


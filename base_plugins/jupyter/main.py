from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget


def definition():
    return PluginDefinition(
        name="jupyter",
        ports=[
            PluginPort(
                internal=8888,
                public=True,
            ),
        ],
        runOn=PluginRunTarget.All,
        execute="jupyter.sh",
        files=[
            "jupyter.sh",
        ],
    )

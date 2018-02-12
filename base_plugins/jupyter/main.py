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
        run_on=PluginRunTarget.All,
        execute="jupyter.sh",
        files=[
            "jupyter.sh",
        ],
    )

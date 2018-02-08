from aztk.plugins import PluginDefinition, PluginPort


def definition():
    return PluginDefinition(
        name="jupyter",
        ports=[
            PluginPort(
             remote=8888,
                local=8888,
            )
        ],
        scripts=[
            "jupyter.sh",
        ]
    )

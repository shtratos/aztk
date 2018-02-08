from aztk.plugins import PluginManifest, PluginPort


def manifest():
    return PluginManifest(
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

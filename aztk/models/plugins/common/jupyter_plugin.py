from aztk.models.plugins.plugin_configuration import PluginConfiguration

class JupyterPlugin(PluginConfiguration):
    def __init__(self):
        super().__init__(
            name="jupyter",
        )

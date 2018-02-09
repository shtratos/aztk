from aztk.plugins import PluginDefinition

class ClusterNotReadyError(Exception):
    pass


class AztkError(Exception):
    def __init__(self, message: str = None):
        super().__init__()
        self.message = message


class AzureApiInitError(AztkError):
    def __init__(self, message: str = None):
        super().__init__()
        self.message = message

class InvalidPluginDefinitionError(AztkError):
    pass

class InvalidModelError(AztkError):
    pass

class InvalidPluginConfigurationError(InvalidModelError):
    def __init__(self, message:str, pluginDefinition: PluginDefinition = None):
        super().__init__(message)
        self.pluginDefinition = pluginDefinition

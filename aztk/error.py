"""
Contains all errors used in Aztk.
All error should inherit from `AztkError`
"""

class ClusterNotReadyError(Exception):
    pass


class AztkError(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)


class AzureApiInitError(AztkError):
    def __init__(self, message: str = None):
        super().__init__()
        self.message = message

class InvalidPluginDefinitionError(AztkError):
    pass

class InvalidModelError(AztkError):
    pass

class MissingRequiredAttributeError(InvalidModelError):
    pass

class InvalidCustomScriptError(InvalidModelError):
    pass

class InvalidPluginConfigurationError(InvalidModelError):
    # from aztk.plugins import PluginDefinition

    def __init__(self, message:str, pluginDefinition = None):
        super().__init__(message)
        self.pluginDefinition = pluginDefinition

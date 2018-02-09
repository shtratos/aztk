from aztk.plugins import PluginDefinition
from aztk.error import InvalidPluginDefinitionError, InvalidPluginConfigurationError


class Plugin:
    def __init__(self, path: str, module):
        """
        Internal container for a plugin.
        :param path: Location of the plugin
        """
        self.path = path
        self.module = module
        self.definition = module.definition()
        if not isinstance(self.definition, PluginDefinition):
            raise InvalidPluginDefinitionError(
                "Plugin {0} definition method doesn't return a PluginDefinition object".
                format(path))
        self.name = self.definition.name

    def validate_args(self, args: dict):
        """
        Validate the given args are valid for the plugin
        """
        self._validate_no_extra_args(args)

        for arg in self.definition.args:
            if args.get(arg.name) is None:
                if arg.required:
                    message = "Missing a required argument {0} for plugin {1}".format(
                        arg.name, self.name)
                    raise InvalidPluginConfigurationError(message)
                args[arg.name] = arg.default

        if hasattr(self.module, "validate_args"):
            try:
                self.module.validate_args(**args)
            except InvalidPluginConfigurationError as e:
                if e.pluginDefinition is None:
                    e.pluginDefinition = self.definition
                raise e

    def process_args(self):
        if hasattr(self.module, "process_args"):
            return self.process_args(**args)
        else:
            return args

    def _validate_no_extra_args(self, args: dict):
        for arg, v in args.items():
            if not self.definition.has_arg(arg):
                message = "Plugin {0} doesn't have an argument called '{1}'".format(
                    self.name, arg)
                raise InvalidPluginConfigurationError(message, self.definition)

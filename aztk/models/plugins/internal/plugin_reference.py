from aztk.error import InvalidPluginConfigurationError


class PluginReference:
    """
    Contains the configuration to use a plugin
    """
    def __init__(self, name, args: dict = None):
        self.name = name
        self.args = args or dict()
        if plugin_manager.has_plugin(self.name):
            self.definition = plugin_manager.get_plugin(self.name).definition

    def plugin(self):
        return plugin_manager.get_plugin(self.name)

    def validate(self) -> bool:
        if not self.name:
            raise error.AztkError("Plugin is missing a name")

        if not self.definition:
            raise error.AztkError(
                "Cannot find a plugin with name '{0}'".format(self.name))
        self.plugin().validate_args(self.args)

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

    def process_args(self, args: dict):
        if hasattr(self.module, "process_args"):
            return self.module.process_args(**args)
        else:
            return args

    def _validate_no_extra_args(self, args: dict):
        for arg, v in args.items():
            if not self.definition.has_arg(arg):
                message = "Plugin {0} doesn't have an argument called '{1}'".format(
                    self.name, arg)
                raise InvalidPluginConfigurationError(message, self.definition)

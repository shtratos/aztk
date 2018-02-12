import argparse
import typing
from cli import log
from aztk.plugins import PluginArgument
from aztk.plugins.internal import plugin_manager


def setup_parser(parser: argparse.ArgumentParser):
    pass


def execute(args: typing.NamedTuple):
    plugins = plugin_manager.plugins
    log.info("------------------------------------------------------")
    log.info("                   Plugins (%i available)",len(plugins))
    log.info("------------------------------------------------------")
    for plugin in plugins.values():
        definition = plugin.definition
        log.info("- %s", plugin.name)
        if definition.args:
            log.info("    Arguments:")
            for arg in definition.args:
                log.info("      - %s", arg_str(arg))
        else:
            log.info("    Arguments: None")
        log.info("")


def arg_str(arg: PluginArgument):
    required = "Required" if arg.required else "Optional(Default: {0})".format(arg.default)
    return "{0}: {1}".format(arg.name, required)

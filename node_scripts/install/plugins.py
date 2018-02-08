import os
import json
import subprocess
from pathlib import Path

def _read_manifest_file(path=None):
    custom_scripts = None
    if not os.path.isfile(path):
        print("Plugins manifest file doesn't exist at {0}".format(path))
    else:
        with open(path, 'r') as stream:
            try:
                custom_scripts = json.load(stream)
            except json.JSONDecodeError as err:
                print("Error in plugins manifest: {0}".format(err))

    return custom_scripts


def setup_plugins(is_master: bool = False, is_worker: bool = False):

    plugins_dir = _plugins_dir()
    plugins_manifest = _read_manifest_file(
        os.path.join(plugins_dir, 'plugins-manifest.json'))

    if plugins_manifest is not None:
        _setup_plugins(plugins_manifest, is_master, is_worker)


def _plugins_dir():
    return os.path.join(os.environ['DOCKER_WORKING_DIR'], 'plugins')


def _run_on_this_node(plugin_obj=None, is_master=False, is_worker=False):
    if plugin_obj['runOn'] == 'master' and is_master is True:
        return True
    if plugin_obj['runOn'] == 'worker' and is_worker is True:
        return True
    if plugin_obj['runOn'] == 'all-nodes':
        return True

    return False


def _setup_plugins(plugins_manifest, is_master=False, is_worker=False):
    plugins_dir = _plugins_dir()

    for plugin in plugins_manifest:
        if _run_on_this_node(plugin, is_master, is_worker):
            path = os.path.join(plugins_dir, plugin['execute'])
            _run_script(path, plugin.get('args'))


def _run_script(script_path: str=None, args: dict = None):
    if not os.path.isfile(script_path):
        print("Cannot run plugin script: {0} file does not exist".format(script_path))
        return
    file_stat = os.stat(script_path)
    os.chmod(script_path, file_stat.st_mode | 0o777)
    print("Running plugin script:", script_path)

    my_env = os.environ.copy()
    if args:
        for [key, value] in args.items():
            my_env[key] = value

    try:
        subprocess.call([script_path], shell=True, env=my_env)
    except Exception as e:
        print(e)

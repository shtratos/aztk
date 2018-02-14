from aztk.models.plugins import PluginDefinition, PluginPort, PluginRunTarget


def test_create_basic_plugin():
    definition = PluginDefinition(
        name="abc", files=["file.sh"], execute="file.sh")
    assert definition.name == "abc"
    assert definition.files == ["file.sh"]
    assert definition.execute == "file.sh"
    assert definition.args == []
    assert definition.run_on == PluginRunTarget.Master


def test_create_with_args():
    definition = PluginDefinition(
        name="abc", args=["arg1", ("arg2", "default-val")])
    assert definition.name == "abc"
    assert len(definition.args) == 2
    assert definition.args[0].required is True
    assert definition.args[0].name == "arg1"
    assert definition.args[0].default is None
    assert definition.args[1].name == "arg2"
    assert definition.args[1].required is False
    assert definition.args[1].default == "default-val"


def test_plugin_with_internal_port():
    definition = PluginDefinition(name="abc", ports=[PluginPort(internal=1234)])
    assert definition.name == "abc"
    assert len(definition.ports) == 1
    port = definition.ports[0]
    assert port.internal == 1234
    assert port.expose_publicly == False
    assert port.public_port == None

def test_plugin_with_auto_public_port():
    definition = PluginDefinition(name="abc", ports=[PluginPort(internal=1234, public=True)])
    assert definition.name == "abc"
    assert len(definition.ports) == 1
    port = definition.ports[0]
    assert port.internal == 1234
    assert port.expose_publicly == True
    assert port.public_port == 1234

def test_plugin_with_specified_public_port():
    definition = PluginDefinition(name="abc", ports=[PluginPort(internal=1234, public=4321)])
    assert definition.name == "abc"
    assert len(definition.ports) == 1
    port = definition.ports[0]
    assert port.internal == 1234
    assert port.expose_publicly == True
    assert port.public_port == 4321

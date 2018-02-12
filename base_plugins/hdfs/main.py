from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget


def definition():
    return PluginDefinition(
        name="hdfs",
        ports=[
            PluginPort(
                internal=8020,
                public=False,
            ),
        ],
        run_on=PluginRunTarget.All,
        execute="hdfs.sh",
        files=[
            "hdfs.sh",
        ],
    )

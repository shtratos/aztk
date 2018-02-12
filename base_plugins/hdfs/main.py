from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget


def definition():
    return PluginDefinition(
        name="hdfs",
        ports=[
            PluginPort(
                name="File system metadata operations",
                internal=8020,
            ),
            PluginPort(
                name="File system metadata operations(Backup)",
                internal=9000,
            ),
            PluginPort(
                name="Datanode data transfer",
                internal=50010,
            ),
            PluginPort(
                name="Datanode IPC metadata operations",
                internal=50020,
            ),
            PluginPort(
                name="Namenode",
                internal=50070,
                public=True,
            ),
            PluginPort(
                name="Datanodes",
                internal=50075,
                public=True,
            ),
        ],
        run_on=PluginRunTarget.All,
        execute="hdfs.sh",
        files=[
            "hdfs.sh",
        ],
    )

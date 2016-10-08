## Plugins module

class PluginError(Exception):
    pass

class BasePlugin(Object):

    def __init__(self):
        """Constructor"""

    def init(self):
        """All plugins must override this method"""
        raise PluginError("init method not overridden")

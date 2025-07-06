class BaseConfigGen:
    def __init__(self):
        self.conf = dict()

    def generate(self):
        """generate the config

        Ex:
            # [ monitor ]
            monitor=,preferred, auto, 2.0
            monitor=,preferred, auto, auto
        """
        configurationfile = "" # only use normal string (do not use f-string)

        for node in self.conf.keys():
            comment = self._add_comment(node)
            configurationfile += comment
            for config in self.conf[node]:
                configurationfile += config + "\n"
        return configurationfile

    def _add_comment(self, node):
        return "\n# [ " + node + " ]\n"


class WaybarConfigGen(BaseConfigGen):
    pass

class HyprConfigGen(BaseConfigGen):
    """
    Manages and generated the config

    example config
    self.conf = {
    monitors: [
        "monitor=eDP-1,1920x1080@60,0x0,1",
        "monitor=eDP-1,preferred,auto,1",
    ],
    exec_once: [
        "waybar"
    ]
    }
    """
    def __init__(self):
        self.conf = dict()
        self.configtree = "" # in future we will add the tree for the available config if the config exists
        # we will cache this and make changes directly to this config and keep it while the system is on

    # General operations
    def add_new_node(self, node, value=None):
        if value is None:
            value = []
        self.conf[node] = value

    def delete_node(self, node):
        if node in self.conf:
            del self.conf[node]

    def update_conf(self, node, value, newvalue):
        if value not in self.conf[node]:
            raise ValueError(
                f"The value: {value} does not exists in node: {node}"
            )
        idx = self.conf[node].index(value)
        self.conf[node][idx] = newvalue

    def remove_conf(self, node, value):
        if value not in self.conf[node]:
            return
        idx = self.conf[node].index(value)
        # I know remove would be more feasible but we can easily avoid error 
        # without any error handling, Avoid error handling where ever I can
        self.conf[node].pop(idx)

    def append_conf(self, node, value):
        self.conf[node].append(value)

    # specific operations
    def exec_command(self, command: str, exec_once=False):
        if exec_once:
            self.append_conf("exec_once", command)
        else:
            self.append_conf("exec", command)

    def keybinds(self, operation, type, value, newvalue=None):
        """add the keybinds to the self.conf

        NOTE: Do not use node operations in keybinds, if you want to use them
        then update the source code first in order to update the keybinds in the
        dictonary.

        Available types:
            1. switching workspace
            2. move active window to workspace
            3. focus to active windows 
            4. Application dispatcher
            5. window actions 
        """
        
        if operation == "add":
            self.conf["keybinds"][type].append(value)

        elif operation == "update":
            if newvalue is None:
                return
            elif value in self.conf["keybinds"][type]:
                self.conf["keybinds"][type] = newvalue

        elif operation == "remove":
            if value in self.conf["keybinds"][type]:
                self.conf["keybinds"][type].remove(value)
        else:
            return

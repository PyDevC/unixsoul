import coredm
import services
import os
import sys
from typing import List

def get_command():
    """This is the most important function where all our commands are read
    from a config file
    Ex: if our hyprland config has  exec python3 launch.py < "rofi"
    Then we get our commands as ["rofi"]
    this is useful as all our commands will be invoked by the window manager
    """
    sys.argv ## higher priority
    sys.stdin
    if type(sys.stdin) == type(str("")):
        stdin = [sys.stdin]
    if sys.argv is List:
        commands = sys.argv + sys.stdin
    else:
        commands = sys.stdin

    return commands

def start(commands):
    """For now it invokes only a single function
    """
    Manager = coredm.manager.HyprlandManager()
    Manager.invokecmd(commands) # just kidding this won't work

commands = get_command()
start(commands)

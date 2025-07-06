#!/usr/bin/python

import coredm
import os
import sys
import subprocess

def askuser(query=None, action=None):
    """Ask user to input something

    Parameters:
        query: question you want to ask or task you want to perform
        action: action you want to take
    
    Returns: json query for performing task
    """
    if query is None:
        query = "Do you want to proceed"
        action = "[y/N]"

    if action is None:
        action = ": "

    print(query, action, end="")
    output = input() # haven't jsonified yet
    return output

def install():
    manager = coredm.manager.HyprlandManager()
    config = coredm.config.HyprConfigGen()

    askuser("do you want to add monitor configuration")
    monitors = ["monitor=,preferred, auto, 2.0", "monitor=,preferred, auto, auto"]
    config.add_new_node("monitor", value=monitors)

    askuser("do you want to add keybindings")
    keybinds = [
                "bind = $mainMod SHIFT, 1, movetoworkspace, 1",
                "bind = $mainMod SHIFT, 2, movetoworkspace, 2",
                "bind = $mainMod SHIFT, 3, movetoworkspace, 3",
                "bind = $mainMod SHIFT, 4, movetoworkspace, 4",
                "bind = $mainMod SHIFT, 5, movetoworkspace, 5",
                "bind = $mainMod SHIFT, 6, movetoworkspace, 6",
                "bind = $mainMod SHIFT, 7, movetoworkspace, 7",
                "bind = $mainMod SHIFT, 8, movetoworkspace, 8",
                "bind = $mainMod SHIFT, 9, movetoworkspace, 9",
    ]
    config.add_new_node("keybindings", value=keybinds)

    print(config.generate())

install()

import os
import sys
import subprocess
from typing import List
import socket
import json

class BaseManager:
    pass

class HyprlandManager(BaseManager):
    def __init__(self):
        self.CONTROLLER = "hyprctl"

        # Change the name later into something relevant
        # The manageunits just keep record of what things is has access to like
        # services and where to look in order to invoke the service
        self.manageunits = {
            "window_manager": "hyprland",
            "services": [] ## will add the services later Do note that this 
                           ## whole things is temporary and can be removed if a method of doing this is found
        }

    def invoke_hyprcmd(self, command):
        """invoke commands
        """
        # NOTE: why use this much functions when we can just invoke directly?
        # its cause we need to invoke other services
        # also there are high chances that the functions will change in order
        # to create a universal manager
        CMDTYPES = {
            "activewindow": self._activewindow,
            "activeworkspace":self._activeworkspace,
            "animations":self._animations,
            "binds":self._binds,
            "clients":self._clients,
            "configerrors":self._configerrors,
            "cursorpos":self._cursorpos,
            "decorations":self._decorations,
            "devices":self._devices,
            "dismissnotify":self._dismissnotify,
            "dispatch":self._dispatch,
            "getoption":self._getoption,
            "globalshortcuts":self._globalshortcuts,
            "hyprpaper":self._hyprpaper,
            "hyprsunset":self._hyprsunset,
            "instances":self._instances,
            "keyword":self._keyword,
            "kill":self._kill,
            "layers":self._layers,
            "layouts":self._layouts,
            "monitors":self._monitors,
            "notify":self._notify,
            "output":self._output,
            "plugin":self._plugin,
            "reload":self._reload,
            "rollinglog":self._rollinglog,
            "setcursor":self._setcursor,
            "seterror":self._seterror,
            "setprop":self._setprop,
            "splash":self._splash,
            "switchxkblayout":self._switchxkblayout,
            "workspacerules":self._workspacerules,
            "workspaces":self._workspaces,
        }

        cmdtype = command[0]
        if command[0] == self.CONTROLLER:
            #CMDTYPES[command[0]](command[1:])
            #for now we are running the commands directly
            output = subprocess.run(command, capture_output=True)
            if output.stdout:
                print(output.stdout)


    def runscript(self, script):
        """only run the scripts whose output can be ommited
        """
        script_path = "script/" + script + ".sh"
        subprocess.run(script_path)

    def _update_config(self):
        pass

    def _activewindow(self, *args):
        pass

    def _activeworkspace(self, *args):
        pass

    def _animations(self, *args):
        pass

    def _binds(self, *args):
        pass

    def _clients(self, *args):
        pass

    def _configerrors(self, *args):
        pass

    def _cursorpos(self, *args):
        pass

    def _decorations(self, *args):
        pass

    def _devices(self, *args):
        pass

    def _dismissnotify(self, *args):
        pass

    def _dispatch(self, *args):
        pass

    def _getoption(self, *args):
        pass

    def _globalshortcuts(self, *args):
        pass

    def _hyprpaper(self, *args):
        pass

    def _hyprsunset(self, *args):
        pass

    def _instances(self, *args):
        pass

    def _keyword(self, *args):
        pass

    def _kill(self, *args):
        pass

    def _layers(self, *args):
        pass

    def _layouts(self, *args):
        pass

    def _monitors(self, *args):
        pass

    def _notify(self, *args):
        pass

    def _output(self, *args):
        pass

    def _plugin(self, *args):
        pass

    def _reload(self, *args):
        pass

    def _rollinglog(self, *args):
        pass

    def _setcursor(self, *args):
        pass

    def _seterror(self, *args):
        pass

    def _setprop(self, *args):
        pass

    def _splash(self, *args):
        pass

    def _switchxkblayout(self, *args):
        pass

    def _workspacerules(self, *args):
        pass

    def _workspaces(self, *args):
        pass

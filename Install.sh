#!/usr/bin/env bash

# Check the hardware
# It says NVIDIA drivers are having issues

# assuming that the minimumm ram requirements are this in hyprland, and all other distributions
# Need to change this

RAM=4 # 4GB
SPACE=50 # 50GB

## Installation configurations
LOGDIR=$HOME/.unixsoul/logs/installation # WE ARE GOING TO CREATE A CALANDER BASED LOGGER
LOGGEN=0
CURRLOGFILE=""

timestamp(){
    local stamp
    if [[ $1 == "logfile" ]]; then
        stamp=`date | awk '{print $3 "-" $2 "-" $7 }'`
    elif [[ $1 == "time" ]]; then
        stamp=`date | awk '{print $4}' | tr ':' '-'`
    elif [[ $1 == "duplicate" ]]; then
        stamp=`date | awk '{print $3 "-" $2 "-" $7 "-" $4}' | tr ':' '-'`
    fi
    echo $stamp
}

log(){
    if [[ -z $CURRLOGFILE ]]; then
        local logname
        mkdir -p $LOGDIR
        cd $LOGDIR
        logname="$(timestamp "logfile").log"
        # Check if the file already exists
        if [[ ! -d "$CURRLOGFILE/$logname" ]]; then
            logname="$(timestamp "duplicate").log"
        fi
        touch $logname
        CURRLOGFILE="$LOGDIR/$logname"
    fi
    printf "$1\n" >> $CURRLOGFILE
}

addEnvToRcfiles(){
    # Adding environment variables to source files such as bashrc, or zshrc
    # read the json file envar_list.json
    # TODO: think about it later (before first release)
    echo "not implemented yet"
}

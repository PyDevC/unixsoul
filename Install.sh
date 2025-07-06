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

checkPackageManager(){
    # This is to be used to update envarlist.json .PACKAGE_MANAGER entry,
    # this funciton is ought to be called only once, which is when first time
    # installing the script, do not run it in any other case
    # Returns package manager that is available
    # If returns None then abort the installation and tell user that no compatible
    # package manager found
    
    if [[ ! -z "$(which apt)" ]]; then
        echo "apt"
    elif [[ ! -z "$(which dnf)" ]]; then
        echo "dnf"
    elif [[ ! -z "$(which pacman)" ]]; then
        echo "pacman"
    else
        echo "None"
    fi
}

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
    # usage:
    # log "this is log example"
    
    if [[ -z $CURRLOGFILE ]]; then
        local logname
        mkdir -p $LOGDIR
        cd $LOGDIR
        logname="$(timestamp "logfile").log"
        # Check if the file already exists
        if [[ -f "$LOGDIR/$logname" ]]; then
            logname="$(timestamp "duplicate").log"
        fi
        touch $logname
        CURRLOGFILE="$LOGDIR/$logname"
    fi
    printf "$1\n" >> $CURRLOGFILE
}

queryEnvarlist(){
    # usage:
    # queryEnvarlist ".DEFAULT.UNIXSOUL"
    # output: $HOME/.unixsoul
    
    if [[ -z "$(which jq)" ]]; then
        sudo $PAC install jq
    fi
    out="$(cat ./envarlist.json | jq -r "$1")"

    echo $out
}

#!/bin/bash
trap 'exit 130' INT
while true ; do
    # Specify the script and log file location
    cd /home/pi/scripts
    python retweet.py >> /home/pi/scripts/retweet.log
    sleep 2m
done

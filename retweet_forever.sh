#!/bin/bash
trap 'exit 130' INT
while true ; do
    # Specify the script file location
    cd /home/pi/retweet_bot
    python retweet.py >> retweet.log
    sleep 2m
done

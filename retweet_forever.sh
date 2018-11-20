#!/bin/bash
trap 'exit 130' INT
while true ; do
    # Specify the script and log file location
    cd /home/pi/retweet_bot
    python retweet.py >> /home/pi/retweet_bot/retweet.log
    sleep 2m
done

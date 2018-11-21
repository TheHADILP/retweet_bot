# Retweet-Bot for Twitter with Twython
This is the source code for my Twitter Bot: https://twitter.com/TLoveBotti

## Installation
```
sudo apt update
sudo apt upgrade
sudo apt install python-setuptools
sudo easy_install pip
sudo pip install twython
```
Clone repository:
```git clone https://github.com/TheHADILP/retweet_bot.git```

## Twitter creds
Now you can set up the API access for your Twitter account on https://developer.twitter.com/en/apps

Enter your API keys in the twitter-creds file:  
Put each item on a separate line and remove all quotes.
```
"Consumer Key"
"Consumer Secret"
"Access Token"
"Access Token Secret"
```
Run the following command to prevent your API credentials being accidentally pushed to git:  
```git update-index --skip-worktree twitter-creds```

## Blacklist
All retweeted Tweet-IDs are saved in the retweet_blacklist file.
This ensures that no duplicate posts are tweeted.

## Execute
Run and test the script with
```python retweet.py```

## Automation with crontab
For automation and logging purposes I wrote a Shell script which executes the Python script in an endless loop.

Assuming your script files lie in the /home/pi/retweet_bot/ folder (change the path according to your file location),
this would go into crontab for automated execution at boot.

```@reboot /home/pi/retweet_bot/retweet_forever.sh```


## Customization
Please change the path variable in retweet_forever.sh according to your file location!

You can customize the retweet.py script as you want (e.g. change the monitored accounts or buzzwords).  
Everything is explained inside the Python script.

__As a precautionary measure, the actual API call is initially commented out.  
So you can test the script in a dry run, and check the logs if everything went well.  
After that you can activate the API call.__

Please note that the sleep interval of two seconds is also only for testing!  
You can change that to the amount of time you want to wait before the next tweet.
```
# Put me to rest, modify this for how often you want me to tweet
  #time.sleep(5400)
  time.sleep(2)
```

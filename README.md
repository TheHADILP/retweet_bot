New version (based on Docker & Python3) can be found here: https://github.com/TheHADILP/docker_retweet_bot
<br><br><br>

# Retweet-Bot for Twitter with Twython
This is the source code for my Twitter Bot: https://twitter.com/TLoveBotti

## Installation
```
sudo apt update
sudo apt upgrade
sudo apt install python-setuptools
sudo easy_install twython
```
Clone repository:
```git clone https://github.com/TheHADILP/retweet_bot.git```

## API credentials
Now you can set up the API access for your Twitter account on https://developer.twitter.com/en/apps

Enter your API credentials in the ```twitter-creds``` file.  
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
All retweeted Tweet-IDs are saved in the ```retweet_blacklist``` file.
This ensures that no duplicate posts are tweeted.

## Execute
Run and test the script with
```python retweet.py```

## Automation with CRON
For automation and logging purposes I wrote a Shell script which executes the Python script in an endless loop.

Assuming your script files are located in the ```/home/pi/retweet_bot/``` folder,
this would go into your Cronjob for automated execution at boot.

```@reboot /home/pi/retweet_bot/retweet_forever.sh```

__Please change the path variable according to your file location (also in ```retweet_forever.sh```)!__

## Customization
You can customize the script as you like (e.g. change the user accounts or buzzwords).  

__CAUTION: The API calls can create a lot of mess on your account (like a lot of retweets). So be warned!__

You can change the amount of time you want to wait before the next tweet.
```
# Wait x amount of time before next tweet
time.sleep(900)
```

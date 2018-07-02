#!/usr/bin/env python
# coding: utf8

import sys, random, time
from twython import Twython, TwythonError

# Create application under https://apps.twitter.com/ and put the "Consumer Key", "Consumer Secret", "Access Token" and "Access Token Secret" in the twitter-creds file in separate lines (also remove all quotes inside twitter-creds)
with open('twitter-creds') as f:
    lines = f.read().splitlines()

api = Twython(*lines)

# List of user accounts to check, modify as you like
users = [
        'alexluyken',
        'StefKch1',
        'KriClement',
        'pepebellin',
        'FrauMagenta',
        'ulrike_die_hex',
        'LudwigMetz1',
        'kaman4010',
        'TelekomStefan',
        'TelekomBotsch',
        'nessa_salberg',
        'PhillipGoik',
        'winfried_ebner',
        'dillinger4010',
        'Mike_4010',
        'MagentaLH',
        'MagentaLeinf',
        'MagentaBerlin',
        'MagentaWOB',
        'SHaderecker',
        'seymen__s',
        'TSWDarmstadt',
        'yem',
        'DTIT_innovation',
        'Nathi_801',
        'DT_IoT',
        'Vids_Mueller',
        'Stef4010',
        'M_Jordan1998',
        'thomasollendorf',
        'JamiieL33',
        'Lehmschicht',
        'JohnLegere',
        'tsystemsde',
        'inklusiv',
        'AndreaPizzato_T',
        'HellwegJonas',
        'schuldmichael',
        'HRickmann',
        'BackofenD',
        'adel_al_saleh',
        'schindera',
        'M_Hagspihl',
        'telekomnetz',
        'telekomerleben',
        'deutschetelekom',
        'AaronTeleK',
        'Life_Is_Magenta',
        'coffeeandsteph'
        ]

while True:
    try:
        if len(users) > 0:
            # Select a random user in the array and remove it until the script restarts
            selected = users[random.randint(0,len(users))-1]
            users.remove(selected)
            print selected

            # Get first tweet from the currently selected user's timeline
            try:
                timeline = api.get_user_timeline(screen_name=selected, count=1, exclude_replies='true', include_rts='true')
            except TwythonError as e:
                print e

            
            for tweet in timeline:
                nId = tweet['id_str']
                
                # List of buzzwords, modify as you like
                buzzwords = ["telekom", "Telekom", "jetztmagenta", "LoveMagenta", "OpenTelekomCloud", "opentelekomcloud", "Develovers", "werkstolz", "ProudToBeT", "magentaverbindet", "YITT", "yitt", "telekomwall", "IoT", "Lehmschicht", "Entertain", "Security", "Glasfaser", "Netz", "Megadeal", "magentamuc"]
                
                # Check if there are any of our specified buzzwords in the tweet text
                if any(n in tweet['text'] for n in buzzwords):
                    
                    # Check if the tweet wasn't already tweeted by us, "old" tweet ids are saved in the retweet_blacklist file
                    if nId not in open('retweet_blacklist').read():
                        # This is a new tweet for us
                        print 'nId: ' + nId
                        print tweet['text'].encode('utf-8')
                        print '     TWEETED!!! (NEW ON MY PROFILE)                  #####'
                        print ''
                        
                        # Write the new tweet id to the blacklist to remember that we already tweeted it
                        with open('retweet_blacklist', 'a') as file:
                            file.write('\n' + nId)
                        
                        # Actually tweet to our account   CAREFULLY: This can also create a lot of mess on your account, better perform a "dry run" and check the console output before removing the #
                        #api.retweet(id = nId)
                        
                        # Put me to rest, modify this for how often you want me to tweet
                        #time.sleep(5400)
                        time.sleep(2)
                    else:
                        # Duplicate found, proceed to the next user in our array
                        print '     DUPLICATE FOUND'
                        
                        # Put me to rest, so I won't exceed API limits
                        time.sleep(2)
                        break
                else:
                    # No buzzwords found in tweet, proceed to the next user in our array
                    print '     NOTHING FOUND YET'
                    
                    # Put me to rest, so I won't exceed API limits
                    time.sleep(2)
                    break
        else:
            # Our user list is empty, end of script
            # See you in the next round when retweet_forever.sh starts us over again
            print 'EMPTY, RESTARTING SCRIPT...'
            break
    except TwythonError as e:
        print e

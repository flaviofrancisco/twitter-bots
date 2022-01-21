# twitter-bots
Some useful Twitter bots in Python

# Dependencies

You need to install the module tweepy in order to use the scripts.

```
pip3 install --user tweepy 
```
# Files

## auth.py

This file is where you will put your credentials from your [Twitter Developers Account](https://developer.twitter.com/en).
For your security never put your token keys explicitly on remote servers.

```python
    auth = tweepy.OAuthHandler(consumer_key='', consumer_secret='')
    auth.set_access_token(key='', secret='')
```

## bot-tech-jobs.py

The goal of this script is to retweet tweets based on the filter from the given parameters of the function: scrape.

```python
 d = datetime.today() - timedelta(days=14)
 scrape(words='(vaga OR vagas) (pj OR clt)  (dev OR desenvolvedor OR UI OR UX OR DevOps OR SRE) R$ -filter:retweets', date_since=d ,numtweet=300, language='pt')  
```
The parameters above fetches the job opportunities with the keywords as you can see on the snippet above that are not retweets from two weeks ago.

## autolike-bot.py

This script is just a simple example on how to autolike tweets where your account was mentioned every 15 seconds.

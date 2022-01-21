import time
import auth
    
MY_LAST_TWEET_FILE = 'my_last_tweet.txt'    

def save_last_tweet(tweet_id):
    with open(MY_LAST_TWEET_FILE, 'w') as f:
        f.write(str(tweet_id))
        f.close()

def read_last_tweet():
    with open(MY_LAST_TWEET_FILE, 'r') as f:
        content = f.read().strip()
        if content != '':
            return int(content)    
        f.close()          

def auto_like():
    api = auth.get_api()

    last_tweet_id = read_last_tweet()
    
    if last_tweet_id != None:
        tweets = list(api.mentions_timeline(since_id=last_tweet_id, tweet_mode='extended'))
    else:
        tweets = list(api.mentions_timeline(tweet_mode='extended'))

    for tweet in reversed(tweets):
        status = api.get_status(tweet.id)
        if status.favorited != True and last_tweet_id != tweet.id:
            save_last_tweet(tweet.id)
            api.create_favorite(tweet.id)

if __name__ == '__main__':
    while True:
        auto_like()
        time.sleep(15)

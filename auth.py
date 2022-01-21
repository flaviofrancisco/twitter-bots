import tweepy

def get_api():
    auth = tweepy.OAuthHandler(consumer_key='', consumer_secret='')
    auth.set_access_token(key='', secret='')
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    pass

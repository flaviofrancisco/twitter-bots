import auth
import tweepy
from datetime import datetime, timedelta

def scrape(words, date_since, numtweet, language):

    tweets = tweepy.Cursor(api.search_tweets,
                    words, lang=language,
                    since_id=date_since,
                    tweet_mode='extended').items(numtweet)
    
    for tweet in tweets:
        status = api.get_status(tweet.id)
        if not status.retweeted:
            api.retweet(tweet.id)


if __name__ == '__main__':   
    api = auth.get_api()
    d = datetime.today() - timedelta(days=14)
    scrape(words='(vaga OR vagas) (pj OR clt)  (dev OR desenvolvedor OR UI OR UX OR DevOps OR SRE) R$ -filter:retweets', date_since=d ,numtweet=300, language='pt')    

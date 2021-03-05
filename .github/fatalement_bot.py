from datetime import datetime, timedelta
import os

import feedparser
import pytz
import tweepy

#Twitter keys
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


def _tweet_article(api, version):
    text = f"A new version of Artemis-css is available! \nYou can read see the version {version} on https://github.com/dianedelallee/artemis"
    print(f'will tweet about the new version of Artemis')
    api.update_status(text)


def get_new_version():
    previous_hour = datetime.today().replace(tzinfo=pytz.utc) - timedelta(hours=1)
    

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # find a way to know that a new version is available
    # called _tweet_article(api, version)
    print('----- END -----')


if __name__ == '__main__':
    get_new_version()

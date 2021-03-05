from datetime import datetime, timedelta
import os

import requests
import tweepy

#Twitter keys
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


def _tweet_article(api, version, link):
    text = f"A new version of Artemis-css is available! \nYou can read see the version {version} on {link}"
    print(f'will tweet about the new version of Artemis')
    api.update_status(text)


def get_new_version():
    previous_hour = datetime.today() - timedelta(hours=6)
    response = requests.get("https://api.github.com/repos/dianedelallee/artemis/releases/latest")
    publication_date = datetime.strptime(response.json()['published_at'], '%Y-%m-%dT%H:%M:%SZ')
    

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    if publication_date >= previous_hour:
        _tweet_article(api, response.json()["tag_name"], response.json()["html_url"])
    print('----- END -----')


if __name__ == '__main__':
    get_new_version()

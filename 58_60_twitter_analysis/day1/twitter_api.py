from collections import namedtuple
import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tweepy
from wordcloud import WordCloud, STOPWORDS


Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_ACCOUNT = 'pybites'

TWITTER_KEY = os.environ['TWITTER_KEY']
TWITTER_SECRET = os.environ['TWITTER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']


auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)


def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exclude_replies=False, include_rts=True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count,
                    tw.retweet_count)


tweets = list(get_tweets())

all_tweets_excl_rts_mentions = ' '.join(
    [tw.text.lower() for tw in tweets if not tw.text.startswith('RT') and not
     tw.text.startswith('@')]
)

pb_mask = np.array(Image.open("pybites.png"))
stopwords = set(STOPWORDS)
stopwords.add('co')
stopwords.add('https')

wc = WordCloud(background_color='white', max_words=2000, mask=pb_mask,
               stopwords=stopwords)

wc.generate(all_tweets_excl_rts_mentions)


plt.figure(figsize=(30, 30))
plt.imshow(wc, interpolation="bilinear")
plt.margins(x=0, y=0)
plt.axis("off")

plt.show()

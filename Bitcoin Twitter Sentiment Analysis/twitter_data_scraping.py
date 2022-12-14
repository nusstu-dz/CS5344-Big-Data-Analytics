# -*- coding: utf-8 -*-
"""Twitter Data Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1em912AFQxLqXtSyWM40fD0hAdm4KF7Dt
"""

!pip install snscrape

import pandas as pd
import numpy as np
import time
import snscrape.modules.twitter as sntwitter

path = ''

maxTweets = 100000

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data
for tweet in sntwitter.TwitterSearchScraper('BTC OR bitcoin lang:en since:2021-10-24 until:2022-03-01').get_items():
    if len(tweets_list)>maxTweets:
        break
    if tweet.likeCount >= 10:
        tweets_list.append([tweet.id,tweet.user.username,tweet.content,tweet.date,tweet.retweetCount,tweet.likeCount,tweet.replyCount])
        print(len(tweets_list))

tweets_df = pd.DataFrame(tweets_list,columns=['Tweet_ID', "Account_Name", 'Text', 'Datetime','Number_Retweets', 'Number_Likes', 'Number_Comments'])
tweets_df.to_csv(path + '/BTC_tweets.csv', mode='a', header=False)
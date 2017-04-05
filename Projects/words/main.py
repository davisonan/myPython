#' % Techniques related to NLP
#' % Xu Tian
#' % 2017/04/04

#' # Overview
#' What are the key issues in natual language processing? The motivation to
#' answer this question is from the need of preparing for the data scientist
#' interview at BlackRock in Shimon's team. He asked me questions around text
#' mining or other text related questions since these will be heavily used about
#' human analytics.

#' # Text mining
#' - Information retrieval:
#' - Named entity recognition:
#' - Sentiment analysis:

#' ## Information retrieval
#'

#' # Performance and correctness measures
#' - Precision: (also called positive predictive value) is the fraction of the
#' documents retrieved that are relevant to the user's information need.
#' - True positive rate:

#' # Sentiment analysis of tweets

from __future__ import division
import urllib
import csv
from string import punctuation

files=['negative.txt', 'positive.txt', 'obama_tweets.txt']
path='http://www.unc.edu/~ncaren/haphazard/'
for file_name in files:
    urllib.request.urlretrieve(path+file_name, file_name)

tweets = open("obama_tweets.txt").read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt").read()
positive_words = pos_sent.split('\n')
positive_counts = []

neg_sent = open('negative.txt').read()
negative_words = neg_sent.split('\n')
negative_counts = []

for tweet in tweets_list:
    positive_counter = 0
    negative_counter = 0
    tweet_processed = tweet.lower()
    for p in list(punctuation):
        tweet_processed = tweet_processed.replace(p, '')

    words = tweet_processed.split(' ')
    word_count = len(words)
    for word in words:
        if word in positive_words:
            positive_counter = positive_counter + 1
        elif word in negative_words:
            negative_counter = negative_counter + 1

    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print(len(positive_counts))

output = list(zip(tweets_list, positive_counts, negative_counts))
writer = csv.writer(open('tweet_sentiment.csv', 'w'))
writer.writerows(output)

def calStd(l):
    n = len(l)
    avg = sum(l)/n
    return sqrt(sum([(i-avg)**2 for i in l])/n)

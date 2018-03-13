#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:56:52 2018

@author: samehamin
"""

from __future__ import division
from collections import defaultdict
import sys
import json



def get_scores(sentiment_file):

    # fill the sentiment dic
    with open(sentiment_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def tweet_score(tweet, scores):
    
    # calc sentiment scores
    return sum(scores.get(word, 0) for word in tweet.split())


def get_tweet_data(tweet):
    try:
        country = tweet['place']['country_code']
        state = tweet['place']['full_name'].split(", ")[1]
        text = tweet['text']
        return country, state, text
    except (KeyError, TypeError, IndexError):
        return None


def happiest_state(tweet_file, scores):
     n_tweets, scores, happiness = [defaultdict(float) for _ in range(3)]
     
     with open(tweet_file) as f:
         tweets = (json.loads(line) for line in f)
         
         parsed_tweets = (get_tweet_data(tweet) 
             for tweet in tweets if get_tweet_data(tweet))
         
         states_scores = ((state, tweet_score(text, scores))
                         for country, state, text in parsed_tweets
                         if country == 'US')
         
         for state, score in states_scores:
            n_tweets[state] += 1
            scores[state] += score
            happiness[state] = scores[state] / n_tweets[state]
         
         return states_scores


if __name__ == '__main__':
    scores = get_scores(sentiment_file=sys.argv[1])
    tweet_file = sys.argv[2]
    print (happiest_state(tweet_file=tweet_file, scores=scores))


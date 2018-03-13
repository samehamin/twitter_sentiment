#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:56:58 2018

@author: samehamin
"""


from __future__ import division
import sys
import json



def get_scores(sentiment_file):

    # fill the sentiment dic
    with open(sentiment_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def tweet_score(tweet, scores):

    # calc sentiment scores
    return sum(scores.get(word, 0) for word in tweet)


def missing_score_word(tweets_file, scores):
    missing_dict = {}
    
    with open(tweets_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)

        for tweet in tweets:
            missing_dict.update({word: tweet_score(tweet, scores) / len(tweet)
                    for word in tweet if word not in scores})

    return missing_dict


if __name__ == '__main__':
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    scores = get_scores(sentiment_file=sent_file)
    missing_scores_dic = missing_score_word(tweet_file, scores=scores)
    
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in missing_scores_dic.items())

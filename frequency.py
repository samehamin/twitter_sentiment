#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:56:58 2018

@author: samehamin
"""

from __future__ import division
import sys
import json
from collections import Counter


def get_frequency(tweet_file):
    with open(tweet_file) as f:
         tweets = (json.loads(line).get('text', '').split() for line in f)
         counter = Counter()
         for tweet in tweets:
             counter.update({word for word in tweet})
         return counter


if __name__ == '__main__':
    tweets = sys.argv[1]
    
    frequencies = get_frequency(tweet_file=tweets)
    
    total_freq = sum(frequencies.values())
    
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), frequencies[word]/total_freq)
    for word in frequencies)

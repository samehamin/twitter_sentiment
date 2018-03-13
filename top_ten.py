#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:21:37 2018

@author: samehamin
"""

import sys
import json
from collections import Counter


def get_top_ten(tweet_file):
    with open(tweet_file) as f:
        entities = (json.loads(line).get('entities', None) for line in f)
        tweet_hashtags = (entity.get('hashtags') for entity in entities if entity)
        texts = (tag['text'] for hashtags in tweet_hashtags for tag in hashtags)
        texts = (text.encode('utf-8') for text in texts)
        return Counter(texts).most_common(10)


if __name__ == '__main__':
    top_ten = get_top_ten(tweet_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}.0\n'.format(key, value) for key, value in top_ten)
import sys
import json


def get_scores(sentiment_file):

    # fill the sentiment dic
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def tweet_score(tweet, scores):

    # calc sentiment scores
    return sum(scores.get(word, 0) for word in tweet.split())


def tweet_scores(tweet_file, scores):

    # Calculate scores of all tweets
    tweets = open(tweet_file)
    tweets_all_scores = []
    
    for tweet in tweets:
        tweet = json.loads(tweet).get('text', '')
        tweet_score(tweet, scores)
        tweets_all_scores.append(tweet_score(tweet, scores))

    return tweets_all_scores


if __name__ == '__main__':
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = get_scores(sentiment_file=sent_file)
    sys.stdout.writelines('{0}.0\n'.format(score)
                          for score in tweet_scores(tweet_file=tweet_file, scores=scores))

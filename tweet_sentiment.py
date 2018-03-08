import sys
import json


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


# Get the sentiments
def generateSentimentDic(f_sentiment):

    scores = {} # initialize an empty dictionary
    for line in f_sentiment:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    

# Generate tweets sentiments
def generate_tweets_sent(tweet_file, sent_scores):

    for tweet in tweet_file:
        sum = 0
        
        try:
            tweet = json.loads('utf-8')
            print tweet
        except ValueError:
            pass

"""        if 'text' in tweet:
            print tweet
            text = tweet['text']
"""

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = generateSentimentDic(sent_file)
    generate_tweets_sent(tweet_file, scores)


if __name__ == '__main__':
    main()

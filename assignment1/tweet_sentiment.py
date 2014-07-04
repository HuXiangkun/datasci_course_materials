import sys
import json

scores = {}
tweets = []

def loadAFINN(sent_file):
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)


def loadTwitts(tweet_file):
    for line in tweet_file.readlines():
        t = json.loads(line)
        if t.has_key("created_at"):
            tweets.append(t['text'].encode('utf-8'))

def printSentiment():
    for tweet in tweets:
        score = 0
        words = []
        words = tweet.split(" ")
        for word in words:
            if word in scores.keys():
                score += scores[word]
        print score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadAFINN(sent_file)
    loadTwitts(tweet_file)
    printSentiment()

if __name__ == '__main__':
    main()

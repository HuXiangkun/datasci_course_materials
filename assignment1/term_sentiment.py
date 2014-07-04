from __future__ import division
import sys
import json

scores = {}
tweets = []
tweet_score = {}
terms = {}

def loadAFINN(sent_file):
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)


def loadTwitts(tweet_file):
    for line in tweet_file.readlines():
        t = json.loads(line)
        if t.has_key("created_at"):
            tweets.append(t['text'].encode('utf-8'))

def getTweetScore():
    for tweet in tweets:
        positiveCount = 0.1
        nagtiveCount = 0.1
        words = []
        words = tweet.split(" ")
        for word in words:
            if word in scores.keys():
                if scores[word]>0:
                    positiveCount += scores[word]
                else:
                    nagtiveCount -= scores[word]
        tweet_score[tweet] = positiveCount/nagtiveCount

def printTermSentiment():
    for tweet in tweets:
        words = tweet.split(" ")
        for word in words:
            score = 0.0
            count = 0
            for tweet1 in tweets:
                ws = tweet1.split(" ")
                if word in ws:
                    score += tweet_score[tweet1]
                    count += 1
                    terms[word] = (score,count)
    for term in terms.keys():
        tp = terms[term]
        s = tp[0]/tp[1]
        print "%s %f" % (term,s)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadAFINN(sent_file)
    loadTwitts(tweet_file)
    getTweetScore()
    printTermSentiment()

if __name__ == '__main__':
    main()

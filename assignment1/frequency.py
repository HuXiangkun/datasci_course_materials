from __future__ import division
import sys
import json

tweets = []
terms = {}

def loadTwitts(tweet_file):
    for line in tweet_file.readlines():
        t = json.loads(line)
        if t.has_key("created_at"):
            tweets.append(t['text'].encode('utf-8'))

def getTerms():
    for tweet in tweets:
        words = tweet.split(' ')
        for word in words:
            if len(word)>0 and len(word.split(" "))==1 and word!='\n' and word!="":
               terms.setdefault(word,0)
               terms[word] += 1

def printTermFrequency():
    totalCount = 0
    for frequency in terms.values():
        totalCount += frequency
    for term in terms.keys():
        t = repr(term)
        s = t.replace("\'",'') + " " + str(terms[term]/totalCount)
        if len(s.split(' ')) == 2:
           print s

def main():
    tweet_file = open(sys.argv[1])
    loadTwitts(tweet_file)
    getTerms()
    printTermFrequency()


if __name__ == '__main__':
    main()

import sys
import json

hashtags = {}

def loadTwitts(tweet_file):
    for line in tweet_file.readlines():
        t = json.loads(line)
        if t.has_key("created_at") and t.has_key("entities"):
            htags = t["entities"]["hashtags"]
            for h in htags:
                if h.has_key("text"):
                    text = h["text"].encode('utf-8')
                    hashtags.setdefault(text,0)
                    hashtags[text] += 1

def printTopTen():
    hs = hashtags.items()
    hs.sort(key = lambda x:x[1],reverse = True)
    for h in hs[:10]:
        print h[0] + " " + str(h[1])

def main():
    tweet_file = open(sys.argv[1])
    loadTwitts(tweet_file)
    printTopTen()


if __name__ == '__main__':
    main()

import sys
import json

states = {
        'ak': 'alaska',
        'al': 'alabama',
        'ar': 'arkansas',
        'as': 'american samoa',
        'az': 'arizona',
        'ca': 'california',
        'co': 'colorado',
        'ct': 'connecticut',
        'dc': 'district of columbia',
        'de': 'delaware',
        'fl': 'florida',
        'ga': 'georgia',
        'gu': 'guam',
        'hi': 'hawaii',
        'ia': 'iowa',
        'id': 'idaho',
        'il': 'illinois',
        'in': 'indiana',
        'ks': 'kansas',
        'ky': 'kentucky',
        'la': 'louisiana',
        'ma': 'massachusetts',
        'md': 'maryland',
        'me': 'maine',
        'mi': 'michigan',
        'mn': 'minnesota',
        'mo': 'missouri',
        'mp': 'northern mariana islands',
        'ms': 'mississippi',
        'mt': 'montana',
        'na': 'national',
        'nc': 'north carolina',
        'nd': 'north dakota',
        'ne': 'nebraska',
        'nh': 'new hampshire',
        'nj': 'new jersey',
        'nm': 'new mexico',
        'nv': 'nevada',
        'ny': 'new york',
        'oh': 'ohio',
        'ok': 'oklahoma',
        'or': 'oregon',
        'pa': 'pennsylvania',
        'pr': 'puerto rico',
        'ri': 'rhode island',
        'sc': 'south carolina',
        'sd': 'south dakota',
        'tn': 'tennessee',
        'tx': 'texas',
        'ut': 'utah',
        'va': 'virginia',
        'vi': 'virgin islands',
        'vt': 'vermont',
        'wa': 'washington',
        'wi': 'wisconsin',
        'wv': 'west virginia',
        'wy': 'wyoming'
}


scores = {}
tweets = []
tweet_score = {}
locations = []

def loadAFINN(sent_file):
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)


def loadTwitts(tweet_file):
    for line in tweet_file.readlines():
        t = json.loads(line)
        if t.has_key("created_at"):
            tweet = t['text'].encode('utf-8')
            place_name = ""
            user_location = ""
            if t["place"]!= None and t["place"].has_key("name"):
                place_name = t["place"]["name"].lower()
            if t["user"]!=None and t["user"].has_key("location"):
                user_location = t["user"]["location"].lower()
            if (len(place_name)>2 and (place_name in states.values())):
                tweets.append(tweet)
                for item in states.items():
                    if place_name == item[1]:
                        locations.append(item[0])
                        break
            elif (len(place_name)==2 and place_name in states.keys()):
                tweets.append(tweet)
                locations.append(place_name)
            elif (len(user_location)>2 and (user_location in states.values())):
                tweets.append(tweet)
                for item in states.items():
                    if user_location == item[1]:
                        locations.append(item[0])
                        break
            elif (len(user_location)==2 and user_location in states.keys()):
                tweets.append(tweet)
                locations.append(user_location)


def getSentiment():
    for tweet in tweets:
        score = 0
        words = []
        words = tweet.split(" ")
        for word in words:
            if word in scores.keys():
                score += scores[word]
        tweet_score[tweet] = score

def printHappiestState():
    h = tweet_score[tweets[0]]
    i = 0
    index = 0
    for tweet in tweets:
        if tweet_score[tweet] > h:
            index = i
        i += 1
    print locations[index].upper()

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadAFINN(sent_file)
    loadTwitts(tweet_file)
    getSentiment()
    printHappiestState()

if __name__ == '__main__':
    main()

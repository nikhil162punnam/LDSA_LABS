import sys
import json

unique_tweets = 0

for line in sys.stdin:
    try:
        each_tweet = json.loads(line)
    except:
        continue
    word_list = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
    word_count = {}
    if not each_tweet['retweeted']:
        unique_tweets += 1
        text = each_tweet['text'].lower()
        for eachword in word_list:
            tcount =  text.count(eachword)
            if tcount > 0:
                word_count[eachword] = tcount
    [print(wc,1) for wc in word_count]

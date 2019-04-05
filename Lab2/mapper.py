#!/usr/bin/env python3


import sys
import json


for line in sys.stdin:
    if len(line) != 1:
        each_tweet = json.loads(line)
        word_list = {'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'}
        word_count = {}
        if not each_tweet['retweeted']:
            text = each_tweet['text'].lower()
            for eachword in word_list:
                tcount =  text.count(eachword)
                if tcount > 0:
                    word_count[eachword] = tcount
            if len(word_count) > 0:
                for word in word_count:
                    print('%s\t%s' % (word, 1))
                print('%s\t%s' % ('unique',1))

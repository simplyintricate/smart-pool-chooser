#!/usr/bin/python

import json
import urllib

LTC_TIMEOUT = 10800
TAG_TIMEOUT = 900

tag_hash_faster_link = 'http://tag.hashfaster.com/index.php?page=api&action=gettimesincelastblock&api_key=29c14a879e901f304a82fa5b97735b7c0032638cce8e3bd54e6d9e7bf8f8e9e6&id=488'
ltc_hash_faster_link = 'http://ltc.hashfaster.com/index.php?page=api&action=gettimesincelastblock&api_key=40a66486837fd754d275475eefcf6d4bac86e8928cc2312ac34c55cc4e824440&id=1305'

f = urllib.urlopen(tag_hash_faster_link)
tag_hash_faster_json = f.read()
f = urllib.urlopen(ltc_hash_faster_link)
ltc_hash_faster_json = f.read()

decoded_tag = json.loads(tag_hash_faster_json)
decoded_ltc = json.loads(ltc_hash_faster_json)

tag_time = decoded_tag['gettimesincelastblock']['data']
ltc_time = decoded_ltc['gettimesincelastblock']

if ltc_time < LTC_TIMEOUT:
	print "choose ltc"
elif tag_time < TAG_TIMEOUT:
	print "choose tag"
else:
	print "choose hypernova"


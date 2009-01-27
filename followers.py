#!/usr/bin/python
import twitter
import sys
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')
username = config.get('secrets','username')
password = config.get('secrets','password')
api = twitter.Api(username=username,password=password)
print "Followers:"
for u in api.GetFollowers():
	print u.screen_name;


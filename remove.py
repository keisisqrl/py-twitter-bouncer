#!/usr/bin/python
import twitter
import sys
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')
username = config.get('secrets','username')
password = config.get('secrets','password')
friend = sys.argv[1]
api = twitter.Api(username=username,password=password)
api.DestroyFriendship(user)

#!/usr/bin/python
import twitter
import sys
import secret
api = twitter.Api(username=secret.login,password=secret.password)
users = api.GetFriends()
print "Friends:"
for u in users:
	print u.screen_name;


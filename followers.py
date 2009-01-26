#!/usr/bin/python
import twitter
import secret
import sys
api = twitter.Api(username=secret.login,password=secret.password)
users = api.GetFollowers()
print "Followers:"
for u in users:
	print u.screen_name;


#!/usr/bin/python
import twitter
import secret
import sys
user = sys.argv[1]
api = twitter.Api(username=secret.login,password=secret.password)
api.CreateFriendship(user)

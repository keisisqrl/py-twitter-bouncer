#!/usr/bin/python
import twitter
import sys
import secret
user = sys.argv[1]
api = twitter.Api(username=secret.login,password=secret.password)
api.DestroyFriendship(user)

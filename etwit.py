#!/usr/bin/python
import twitter
import secret
api = twitter.Api(username=secret.login,password=secret.password)
dm = api.GetDirectMessages()

for message in dm:
	api.PostUpdate(message.text + " -from " + message.sender_screen_name)
	api.DestroyDirectMessage(message.id)

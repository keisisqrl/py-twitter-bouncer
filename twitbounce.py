#!/usr/bin/python
import twitter
import secret
api = twitter.Api(username=secret.login,password=secret.password)
dm = api.GetDirectMessages()
id=true

for message in dm:
	newpost = message.text
	if (id):
		newpost = newpost + " -from " + message.sender_screen_name
	api.PostUpdate(newpost)
	api.DestroyDirectMessage(message.id)

#!/usr/bin/python
import twitter
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')
username = config.get('secrets','username')
password = config.get('secrets','password')
anon = config.getboolean('settings','anonymous')
api = twitter.Api(username=username,password=password)
dm = api.GetDirectMessages()

for message in dm:
	newpost = message.text
	if not anon:
		newpost = newpost + " -from " + message.sender_screen_name
	api.PostUpdate(newpost)
	api.DestroyDirectMessage(message.id)

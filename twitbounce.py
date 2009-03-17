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
	try:
		api.PostUpdate(newpost)
	except twitter.TwitterError as e:
		if anon:
			api.PostDirectMessage(user=message.sender_id,text="Error:" + e)
		if not anon:
			api.PostDirectMessage(user=message.sender_id,text="Error:Text must be less than or equal to " + (140 - (len(message.sender_screen_name) + 7)) + " characters.")
	api.DestroyDirectMessage(message.id)

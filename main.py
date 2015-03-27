#!/usr/bin/env python

import json
import webapp2
from google.appengine.ext import ndb

class Message(ndb.Model):
	message = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	message_query = Message.query()
    	messages = [message.to_dict() for message in message_query]
    	self.response.headers['Content-Type'] = 'application/json'
    	# self.response.write(messages)
        json.dump(messages,self.response.out)


class postMessageHandler(webapp2.RequestHandler):
	def get(self):
		message = self.request.get('message')
		msg = Message(message = message)
		msg.put()
		self.response.headers['Content-Type'] = 'application/json'
		message_query = Message.query()
		messages = [message.to_dict() for message in message_query]
		json.dump(messages, self.response.out)

	def post(self):
		message = self.request.get('message')
		post = Message(message = message)
		post.put()
		self.response.headers['Content-Type'] = 'application/json'
		message_query = Message.query()
		messages = [message.to_dict() for message in message_query]
		json.dump(messages, self.response.out)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/postMessage', postMessageHandler)
], debug=True)

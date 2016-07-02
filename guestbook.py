#!/usr/bin/env python

import cgi
import datetime
import webapp2
import os
from google.appengine.ext.webapp import template #also added


class MainPage(webapp2.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    print path
    self.response.out.write(template.render(path, {}))

class LetsEncryptHandler(webapp2.RequestHandler):
  def get(self, challenge):
    self.response.headers['Content-Type'] = 'text/plain'
    responses = {
      'vtBX8y3Y5vmBN5AufTlD0hXYzQf80PP3URfmFwcK87Y': 'vtBX8y3Y5vmBN5AufTlD0hXYzQf80PP3URfmFwcK87Y.OqKVirPRIzhj6SspVJhQSQhHVYvzhHTYuTuKejLZQpU',
      'cWvGL_X0CtZU-XTUrHXl703CEN_g4CE9VBLcp9SCOA8': 'cWvGL_X0CtZU-XTUrHXl703CEN_g4CE9VBLcp9SCOA8.OqKVirPRIzhj6SspVJhQSQhHVYvzhHTYuTuKejLZQpU'
    }
    self.response.write(responses.get(challenge, ''))

app = webapp2.WSGIApplication([
  ('/.well-known/acme-challenge/([\w-]+)', LetsEncryptHandler),
  ('/', MainPage)
], debug=True)

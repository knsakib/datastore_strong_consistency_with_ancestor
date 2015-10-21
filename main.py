#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os

from google.appengine.ext import ndb
import jinja2
import webapp2

from model import database1


jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  autoescape=True)
PARENT_KEY = ndb.Key("Entity","messages")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message_query=database1.query(ancestor=PARENT_KEY).order(-database1.last_touch_date_time)
        
        
        template1= jinja_env.get_template('templates/message.html')
        
        self.response.out.write(template1.render({"message_query":message_query}))
        
        

class saveMessage(webapp2.RedirectHandler):
    def post(self):
        logging.info(str(self.request))
        obj_databasemodel=database1(parent = PARENT_KEY,
                                    email=self.request.get("email"),
                                    message=self.request.get("message"))
        obj_databasemodel.put()
        self.redirect(self.request.referer)
 
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/save_message', saveMessage),
    
], debug=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration of the site"""

import webapp2

from google.appengine.api import users
from controller.project import ProjectList
from controller.project import ProjectNew
from controller.project import ProjectDelete
from controller.project import ProjectUsers
from controller.item import ItemList
from controller.item import ItemNew

class MainPage(webapp2.RequestHandler):
    """MainPage"""

    def get(self):
        """Gets a user"""
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/project', ProjectList),
    ('/project/new', ProjectNew),
    ('/project/delete', ProjectDelete),
    ('/project/addUser', ProjectUsers),
    ('/project/([^/]+)/items', ItemList),
    ('/project/([^/]+)/items/new', ItemNew),
    ('/project/([^/]+)/items/delete', ItemNew)
], debug=True)
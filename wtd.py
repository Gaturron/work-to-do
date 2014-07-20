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
from controller.item import ItemDelete

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
    webapp2.Route('/', handler=MainPage),
    webapp2.Route('/project', handler=ProjectList),
    webapp2.Route('/project/new', handler=ProjectNew),
    webapp2.Route('/project/delete', handler=ProjectDelete),
    webapp2.Route('/project/addUser', handler=ProjectUsers),
    webapp2.Route('/project/<project_key:[^/]+>/items', handler=ItemList, name='project_key'),
    webapp2.Route('/project/<project_key:[^/]+>/items/new', handler=ItemNew, name='project_key'),
    webapp2.Route('/project/<project_key:[^/]+>/items/delete', handler=ItemDelete, name='project_key')
], debug=True)
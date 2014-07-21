#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration of the site"""

import os
import jinja2
import webapp2

from google.appengine.api import users
from controller.project import ProjectList
from controller.project import ProjectNew
from controller.project import ProjectDelete
from controller.project import ProjectUsers
from controller.item import ItemList
from controller.item import ItemNew
from controller.item import ItemDelete

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), './view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True,
    variable_start_string= '((', 
    variable_end_string= '))')

class MainPage(webapp2.RequestHandler):
    """MainPage"""

    def get(self):
        """Gets a user"""
        user = users.get_current_user()

        if user:

            values = {
                "user" : user
            }

            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(values))
            
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
    #Web
    webapp2.Route('/', handler=MainPage),

    #API REST
    webapp2.Route('/project', handler=ProjectList),
    webapp2.Route('/project/new', handler=ProjectNew),
    webapp2.Route('/project/delete', handler=ProjectDelete),
    webapp2.Route('/project/addUser', handler=ProjectUsers),
    webapp2.Route('/project/<project_key:[^/]+>/items', handler=ItemList, name='project_key'),
    webapp2.Route('/project/<project_key:[^/]+>/items/new', handler=ItemNew, name='project_key'),
    webapp2.Route('/project/<project_key:[^/]+>/items/delete', handler=ItemDelete, name='project_key')
], debug=True)
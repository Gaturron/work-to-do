import os
import webapp2

from google.appengine.api import users
from controller.project import projectList
from controller.project import projectNew
from controller.project import projectDelete
from controller.project import projectUsers
from controller.item import itemList
from controller.item import itemNew
from model.Project import Project

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/project', projectList),
    ('/project/new', projectNew),
    ('/project/delete', projectDelete),
    ('/project/addUser', projectUsers),
    ('/project/([^/]+)/items', itemList),
    ('/project/([^/]+)/items/new', itemNew),
    ('/project/([^/]+)/items/delete', itemNew)
], debug=True)
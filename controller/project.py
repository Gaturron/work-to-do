import cgi
import webapp2
import json

from model.Project import Project
from model.jsonize import jsonize
from google.appengine.api import users

class project(webapp2.RequestHandler):
    """API for project"""

    def get(self):

        user = users.get_current_user()
        projects = Project.all().filter('users =', user).run()

        json = jsonize()

        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(json.to_dict(projects))

    def post(self):

        user = users.get_current_user()
        name = cgi.escape(self.request.get('name'))
        description = cgi.escape(self.request.get('description'))

        project = Project(name= name, description= description)
        project.users.append(user)
        project.put()

        self.response.out.write('ok')

    def delete(self):

        key = cgi.escape(self.request.get('key'))

        project = Project.get(key)
        project.delete()

        self.response.out.write('ok')

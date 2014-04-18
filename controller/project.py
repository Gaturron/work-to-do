import cgi
import webapp2
import json

from model.Project import Project
from model.jsonize import jsonize
from google.appengine.api import users

class projectList(webapp2.RequestHandler):
    """List project"""
    
    def get(self):

        user = users.get_current_user()
        projects = Project.all().filter('users =', user).run()

        json = jsonize()

        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(json.to_dict(projects))

class projectNew(webapp2.RequestHandler):
    """New project"""

    def post(self):

        user = users.get_current_user()
        name = cgi.escape(self.request.get('name'))
        description = cgi.escape(self.request.get('description'))

        project = Project(name= name, description= description)
        project.users.append(user)
        project.put()

        self.response.out.write('ok')

class projectDelete(webapp2.RequestHandler):
    """Delete project"""

    def delete(self):

        user = users.get_current_user()
        projects = Project.all().filter('users =', user).run()

        key = cgi.escape(self.request.get('key'))

        project = Project.get(key)

        if (project in projects):
            project.delete()
            self.response.out.write('ok')
        else:
            self.response.out.write('fail')            

class projectUsers(webapp2.RequestHandler):
    """methods to edit projects users"""

    def post(self):

        user = users.get_current_user()
        key = cgi.escape(self.request.get('key'))
        project = Project.get(key)

        if (user in project.users):
            userMail = cgi.escape(self.request.get('userMail'))
            user = users.User(userMail)

            project.users.append(user)
            project.put()

            self.response.out.write('ok')
        else:
            self.response.out.write('fail')
            
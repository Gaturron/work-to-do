"""Project controller"""
import cgi
import webapp2

from model.Project import Project
from model.jsonize import jsonize
from google.appengine.api import users
from google.appengine.api.datastore import Key

class ProjectList(webapp2.RequestHandler):
    """List project"""
    
    def get(self):

        user = users.get_current_user()

        projects = Project.all(keys_only=True).filter('users =', user).run()
        print projects

        json = jsonize()

        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(json.to_dict(projects))
        
class ProjectNew(webapp2.RequestHandler):
    """New project"""

    def post(self):

        user = users.get_current_user()
        name = cgi.escape(self.request.get('name'))
        description = cgi.escape(self.request.get('description'))

        project = Project(name= name, description= description)
        project.users.append(user)
        project.put()

        self.response.out.write('ok')

class ProjectDelete(webapp2.RequestHandler):
    """Delete project"""

    def post(self):

        user = users.get_current_user()
        key = Key(cgi.escape(self.request.get('key')))

        projects = Project.all()
        projects.filter('users =', user)
        projects.filter('__key__ = ', key)
        projects.run()

        project = projects.fetch(1)
        
        if project:
            project[0].delete()
            self.response.out.write('ok')

        else:
            self.response.out.write('fail')            

class ProjectUsers(webapp2.RequestHandler):
    """methods to edit projects users"""

    def post(self):

        user = users.get_current_user()
        key = cgi.escape(self.request.get('key'))
        project = Project.get(key)

        if (user in project.users):
            user_mail = cgi.escape(self.request.get('userMail'))
            user = users.User(user_mail)

            project.users.append(user)
            project.put()

            self.response.out.write('ok')
        else:
            self.response.out.write('fail')
            
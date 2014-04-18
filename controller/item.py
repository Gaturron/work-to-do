import cgi
import webapp2
import json

from model.Project import Project
from model.Item import Item
from model.jsonize import jsonize
from google.appengine.api import users

class itemList(webapp2.RequestHandler):
    """List Items"""

    def get(self, projectKey):

        projectKey = cgi.escape(projectKey)
        project = Project.get(projectKey)

        items = Item.all().filter('project =', project).run()

        json = jsonize()

        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(json.to_dict(items))

class itemNew(webapp2.RequestHandler):
    """New Item"""

    def post(self, projectKey):

        projectKey = cgi.escape(projectKey)
        project = Project.get(projectKey)

        name = cgi.escape(self.request.get('name'))
        description = cgi.escape(self.request.get('description'))

        item = Item(name= name, description= description, project= project)
        item.put()

        self.response.out.write('ok')

class itemDelete(webapp2.RequestHandler):
    """Delete Item"""

    def post(self, projectKey):

        projectKey = cgi.escape(projectKey)
        project = Project.get(projectKey)

        items = Item.all().filter('project =', project).run()

        ItemKey = cgi.escape(self.request.get('ItemKey'))
        item = Item.get(ItemKey)

        if (item in items):
            item.delete()
            self.response.out.write('ok')
        else:
            self.response.out.write('fail')
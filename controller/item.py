"""Item controller"""
import cgi
import webapp2

from model.Project import Project
from model.Item import Item
from model.jsonize import jsonize

class ItemList(webapp2.RequestHandler):
    """List Items"""

    def get(self, project_key):

        project_key = cgi.escape(project_key)
        project = Project.get(project_key)
        print project

        items = Item.all()
        items.filter('project =', project)
        items.run()

        json = jsonize()

        items_list = []    
        for item in items:
            items_list.append(json.to_dict(item))

        self.response.headers['Content-Type'] = 'application/json'   
        self.response.out.write(items_list)

class ItemNew(webapp2.RequestHandler):
    """New Item"""

    def post(self, project_key):

        project_key = cgi.escape(project_key)
        project = Project.get(project_key)
        print project

        name = cgi.escape(self.request.get('name'))
        print name
        description = cgi.escape(self.request.get('description'))
        print description

        item = Item(name= name, description= description, project= project)
        item.put()

        self.response.out.write('ok')

class ItemDelete(webapp2.RequestHandler):
    """Delete Item"""

    def post(self, project_key):

        project_key = cgi.escape(project_key)
        project = Project.get(project_key)

        ItemKey = cgi.escape(self.request.get('ItemKey'))

        items = Item.all()
        Items.filter('project =', project)
        Items.filter('__key__= ', ItemKey)
        Items.run()

        item = Items.fetch(1)

        if item:
            item[0].delete()
            self.response.out.write('ok')
        else:
            self.response.out.write('fail')
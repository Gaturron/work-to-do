"""Model for an item, could be like a task"""

from google.appengine.ext import db
from google.appengine.api import users
from model.Project import Project

class Item(db.Model):
    """Items from a project"""

    name = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    users = db.ListProperty(users.User)

    project = db.ReferenceProperty(  Project,
                                     collection_name='items')
"""Module for a project"""

from google.appengine.ext import db
from google.appengine.api import users

class Project(db.Model):
    """Projects to do"""
    
    name = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    users = db.ListProperty(users.User)
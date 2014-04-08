from google.appengine.ext import db

class Project(db.Model):
    """Projects to do"""
    
    name = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    #users = db.ListProperty(db.UserProperty)
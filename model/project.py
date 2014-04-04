from google.appengine.ext import db

class Proyect(db.Model):
	"""Proyects to do"""
	name = db.StringProperty(required=True)
	description = db.StringProperty(required=True)
	users = db.ListProperty(db.UserProperty)

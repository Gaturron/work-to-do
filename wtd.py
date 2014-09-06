#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration of the site"""

import os
import webapp2

from google.appengine.api import users
from controller.project import ProjectList
from controller.project import ProjectNew
from controller.project import ProjectDelete
from controller.project import ProjectUsers
from controller.item import ItemList
from controller.item import ItemNew
from controller.item import ItemDelete

application = webapp2.WSGIApplication([
    #API REST
    webapp2.Route('/project', handler=ProjectList),
    webapp2.Route('/project/new', handler=ProjectNew),
    webapp2.Route('/project/delete', handler=ProjectDelete),
    webapp2.Route('/project/addUser', handler=ProjectUsers),
    webapp2.Route('/project/<project_key:[^/]+>/items', handler=ItemList, name='project_key'),
    webapp2.Route('/project/<project_key:[^/]+>/items/new', handler=ItemNew, name='project_key'),
    webapp2.Route('/project/<project_key:[^/]+>/items/delete', handler=ItemDelete, name='project_key')
], debug=True)
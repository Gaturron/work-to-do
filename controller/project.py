import webapp2
import json

class project(webapp2.RequestHandler):
  def get(self):
    
    self.response.headers['Content-Type'] = 'application/json'   
    obj = { 'success': 'some var', 
            'payload': 'some var',
    } 
    self.response.out.write(json.dumps(obj))	

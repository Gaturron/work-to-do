"""jsonize"""

from google.appengine.ext import db

class jsonize():
    """Model GAE to Json"""

    def to_dict(self, obj):
    	"""	obj to JSON	"""
        
        if isinstance(obj, db._QueryIterator):
            #return dict([(i, self.to_dict(x)) for i, x in enumerate(obj) ])
            return [ self.to_dict(x) for x in obj ]
        elif isinstance(obj, list):
    		return [ self.to_dict(x) for x in obj ]
        else:	
            return dict([(p, unicode(getattr(obj, p))) for p in 
            	obj.properties()])
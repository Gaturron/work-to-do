from google.appengine.ext import db

class jsonize():
    """Model GAE to Json"""

    def to_dict(self, obj):
        if isinstance(obj, db.Query):
            return dict([(i, self.to_dict(x)) for i, x in enumerate(obj) ])
        else:
            return dict([(p, unicode(getattr(obj, p))) for p in obj.properties()])
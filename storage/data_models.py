from mongoengine import *
import json
from bson import ObjectId



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class News(Document):
    Id = StringField(required=True, max_length=300)
    url = StringField(required=True)
    text = StringField(required=True, max_length=50000)
from mongoengine import *
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class News(Document):
	domain= StringField(required=True, max_length=300)
	language= StringField(required=True, max_length=100)
	title= StringField(required=True, max_length=300)
	imageUrl= StringField(required=True, max_length=1000)
	country = StringField(required=True, max_length=300)
	date = StringField(required=True, max_length=300)
	url = StringField(required=True)
	text = StringField(required=False, max_length=50000)

# {
#         "domain": "express.co.uk",
#         "language": "English",
#         "title": "Sadiq Khan demands London Tories SUPPORT customs union with warning theyll LOSE seat | united kingdom | News",
#         "url": "https://www.express.co.uk/news/uk/934499/sadiq-khan-brexit-london-customs-union",
#         "socialimage": "https://cdn.images.express.co.uk/img/dynamic/1/750x445/934499.jpg",
#         "sourcecountry": "United Kingdom",
#         "seendate": "20180320T160000Z",
#         "url_mobile": "https://www.express.co.uk/news/uk/934499/sadiq-khan-brexit-london-customs-union/amp"
# }
from tornado.web import StaticFileHandler

from handlers import index, travel
from settings import STATIC_PATH


URLS = [
    (r'^/api', index.IndexHandler),
    (r'^/travel', travel.MapHandler),
    (r'/(.*)', StaticFileHandler,
     {'path': STATIC_PATH, 'default_filename': 'index.html'})
]

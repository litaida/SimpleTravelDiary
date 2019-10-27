# Tornado HttpServer
import sys
from tornado import web, ioloop, httpserver

from urls import URLS
from settings import CONFIG, BASE_PATH


if BASE_PATH not in sys.path:
    sys.path.insert(0, BASE_PATH)


class Application(web.Application):
    def __init__(self):
        super(Application, self).__init__(URLS, **CONFIG)


if __name__ == '__main__':
    app = Application()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(80)
    ioloop.IOLoop.current().start()

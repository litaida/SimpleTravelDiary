# Tornado HttpServer
from tornado import web, ioloop, httpserver

from urls import URLS
from settings import CONFIG


class Application(web.Application):
    def __init__(self):
        super(Application, self).__init__(URLS, **CONFIG)


if __name__ == '__main__':
    app = Application()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(80)
    ioloop.IOLoop.current().start()

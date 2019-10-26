# 网站首页逻辑
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    """
    网站首页 - 个人简历
    """
    def get(self):
        self.render('index.html')

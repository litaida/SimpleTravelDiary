# 旅行日记页逻辑
from tornado.web import RequestHandler


class MapHandler(RequestHandler):
    """
    旅行日记 - 地图标注
    """
    def get(self):
        self.render('travel.html')

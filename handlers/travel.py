# 旅行日记页逻辑
import json
from tornado.web import RequestHandler
from models import TravelLocation


class MapHandler(RequestHandler):
    """
    旅行日记 - 地图标注
    """
    def get(self):
        """直接访问页面"""
        self.render('travel.html')

    def post(self):
        """查询某个省份的旅行标注"""
        if self.request.body_arguments:
            post_data = self.request.body_arguments
            province_data = {x: post_data.get(x)[0].decode('UTF-8')
                             for x in post_data.keys()}
        else:
            post_data = self.request.body.decode('UTF-8')
            province_data = json.load(post_data)
        # 接收到省份之后, 查询数据库是否存在对应的标注
        province = province_data.get('Province')
        if not province:
            self.finish({'message': '参数错误, 没有传入省份'})
        province_note = TravelLocation.get_by_province(province)
        print('pn = %s, type = %s' % (str(province_note), type(province_note)))
        if province_note:
            message = str(province_note[0])
            print('返回的数据是: %s' % message)
            self.finish({'message': message})
        else:
            print('返回的数据是: %s' % province)
            self.finish({'message': '参数正确, 省份为: %s' % province})

    def put(self):
        """新增某个省份的旅行标注"""
        self.finish({'message': '新增成功'})

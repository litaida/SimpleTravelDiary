# 旅行日记页逻辑
import json
from traceback import format_exc
from tornado.web import RequestHandler
from models import TravelLocation, create_note, delete_note


class MapHandler(RequestHandler):
    """
    旅行日记 - 地图标注
    """
    def get(self):
        """直接访问页面 或 传入省份以查询对应的旅行标注"""
        province = self.get_query_argument('Province', None)
        print('>>> 进入 GET, 参数: %s' % ('Province = ' + str(province)))
        if province:
            # 接收到省份之后, 查询数据库是否存在对应的标注
            province_note = TravelLocation.get_by_province(province)
            if province_note:
                row = province_note[0]
                status_code = 200
                message = {
                    'province': row.province,
                    'note': row.note,
                    'created_at': row.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
            else:
                status_code = 404
                message = dict()
            p = {
                'status': status_code,
                'message': json.dumps(message, ensure_ascii=False)
            }
            self.finish(p)
        else:
            self.render('travel.html')

    def post(self):
        """新增某个省份的旅行标注"""
        post_data = self.request.body_arguments
        post_data = {x: post_data.get(x)[0].decode('UTF-8')
                         for x in post_data.keys()}
        print('>>> 进入了 POST, 参数: %s' % str(post_data))
        # 接收到相关数据后, 进行写库操作
        try:
            option = post_data.get('method')
            province = post_data.get('province')
            if not province:
                msg = '标注不成功, 主键缺失: %s' % str(province)
                self.finish({'status': 400, 'message': msg})
                return
            if option == 'DELETE':
                delete_note(province)
            else:
                note = post_data.get('note')
                # 检查存在性
                beingness = TravelLocation.get_by_province(province)
                if beingness:
                    self.finish({'status': 403, 'message': '已存在'})
                create_note(province, note)
                print({'status': 200, 'message': '新增成功'})
            self.render('travel.html')
        except:
            print(format_exc())
            self.finish({'status': 500, 'message': '服务器出现错误'})

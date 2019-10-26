# 项目配置文件
import os

# 根目录
BASE_PATH = os.path.dirname(__file__)

# 项目基本设置
CONFIG = dict(
    template_path=os.path.join(BASE_PATH, 'templates'),
    static_path=os.path.join(BASE_PATH, 'static'),
    debug=True,
)

# 静态文件
STATIC_PATH = os.path.join(BASE_PATH, 'static')

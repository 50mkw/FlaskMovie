import os
import configparser
basedir = os.path.abspath(os.path.dirname(__file__))


def get_redis_url():
    config = configparser.ConfigParser()
    config.read(r'cfg/ProjectConfig.ini')
    return 'redis://:{password}@{host}:{port}/1'.format(
        host=config['redis-djangostarmeow']['host'],
        port=config['redis-djangostarmeow']['port'],
        password=config['redis-djangostarmeow']['password'],
    )

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ff72bf399e654310add53d08a164f311'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:Happy@001@127.0.0.1:3306/movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 定义文件上传保存的路径，在__init__.py文件所在目录创建media文件夹，用于保存上传的文件
    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/media/')
    USER_IMAGE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/user/')  # 存放用户头像的路径
    REDIS_URL = get_redis_url()

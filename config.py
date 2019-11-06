import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ff72bf399e654310add53d08a164f311'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:Happy@001@127.0.0.1:3306/movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 定义文件上传保存的路径，在__init__.py文件所在目录创建media文件夹，用于保存上传的文件
    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/media/')

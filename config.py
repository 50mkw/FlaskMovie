import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ff72bf399e654310add53d08a164f311'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:Happy@001@127.0.0.1:3306/movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.home import home as home_blueprint  # 导入
from app.admin import admin as admin_blueprint
from config import Config


app = Flask(__name__)  # 实例化flask
app.debug = True  # 开启调试模式
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
# from app import models
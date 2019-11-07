from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask import render_template


app = Flask(__name__)  # 实例化flask
app.debug = True  # 开启调试模式
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.home import home as home_blueprint  # 导入
from app.admin import admin as admin_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
# from app import models

# 添加全局404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 添加全局401无权限页面
@app.errorhandler(401)
def unauthorized_access(error):
    return render_template('401.html'), 401
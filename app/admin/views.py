from . import admin

# 调用蓝图
@admin.route("/")
def index():
    return "<h1 style='color:red'>后台</h1>"
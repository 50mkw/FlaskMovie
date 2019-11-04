from . import home

# 调用蓝图
@home.route("/")
def index():
    return "<h1 style='color:blue'>前台</h1>"
from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginFrom
from app.models import Admin
from functools import wraps

def admin_login_require(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('login_admin', None) is None:
            # 如果session中未找到该键，则用户需要登录
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

# 调用蓝图
@admin.route("/")
@admin_login_require
def index():
    return render_template('admin/index.html')


@admin.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        # 提交的时候验证表单
        data = form.data  # 获取表单的数据
        # print(data)
        login_admin = Admin.query.filter_by(name=data['account']).first()
        if not login_admin.check_pwd(data['pwd']):
            # 判断密码错误，然后将错误信息返回，使用flash用于消息闪现
            flash('密码错误！')
            return redirect(url_for('admin.login'))
        # 如果密码正确，session中添加账号记录，然后跳转到request中的next，或者是跳转到后台的首页
        session['login_admin'] = data['account']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route("/logout/")
@admin_login_require
def logout():
    session.pop('login_admin', None)  # 删除session中的登录账号
    return redirect(url_for("admin.login"))


@admin.route("/pwd/")
@admin_login_require
def pwd():
    return render_template('admin/pwd.html')


@admin.route("/tag/add/")
@admin_login_require
def tag_add():
    return render_template('admin/tag_add.html')


@admin.route("/tag/list/")
@admin_login_require
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route("/movie/add/")
@admin_login_require
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route("/movie/list/")
@admin_login_require
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route("/preview/add/")
@admin_login_require
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route("/preview/list/")
@admin_login_require
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route("/user/list/")
@admin_login_require
def user_list():
    return render_template('admin/user_list.html')


@admin.route("/user/view/")
@admin_login_require
def user_view():
    return render_template('admin/user_view.html')


@admin.route("/comment/list/")
@admin_login_require
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route("/collect/list/")
@admin_login_require
def collect_list():
    return render_template('admin/collect_list.html')


@admin.route("/logs/operate_log/")
@admin_login_require
def logs_operate_log():
    return render_template('admin/logs_operate_log.html')


@admin.route("/logs/admin_log/")
@admin_login_require
def logs_admin_log():
    return render_template('admin/logs_admin_log.html')


@admin.route("/logs/user_log/")
@admin_login_require
def logs_user_log():
    return render_template('admin/logs_user_log.html')


@admin.route("/auth/add/")
@admin_login_require
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route("/auth/list/")
@admin_login_require
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route("/role/add/")
@admin_login_require
def role_add():
    return render_template('admin/role_add.html')


@admin.route("/role/list/")
@admin_login_require
def role_list():
    return render_template('admin/role_list.html')


@admin.route("/admin/add/")
@admin_login_require
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route("/admin/list/")
@admin_login_require
def admin_list():
    return render_template('admin/admin_list.html')


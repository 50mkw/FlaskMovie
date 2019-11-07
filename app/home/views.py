from . import home
from flask import render_template, redirect, url_for, flash, session, request
from .forms import RegisterForm, LoginFrom
from app.models import User, UserLog
from werkzeug.security import generate_password_hash
from app import db
import uuid


@home.route("/")
def index():
    return render_template('home/index.html')

@home.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data['name']).first()
        if not user.check_pwd(data['pwd']):
            flash('密码错误', category='err')
            return redirect(url_for('home.login'))
        session['login_user'] = user.name
        session['login_user_id'] = user.id
        userlog = UserLog(
            user_id=user.id,
            ip=request.remote_addr
        )
        db.session.add(userlog)
        db.session.commit()
        return redirect(url_for('home.user'))
    return render_template('home/login.html', form=form)

@home.route('/logout/')
def logout():
    session.pop('login_user', None)
    session.pop('login_user_id', None)
    return redirect(url_for('home.login'))

@home.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data['name'],
            pwd=generate_password_hash(data['pwd']),
            email=data['email'],
            phone=data['phone'],
            uuid=uuid.uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        flash('注册成功', category='ok')
        return redirect(url_for('home.register'))
    return render_template('home/register.html', form=form)

@home.route('/user/')
def user():
    return render_template('home/user.html')

@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')

@home.route('/comments/')
def comments():
    return render_template('home/comments.html')

@home.route('/userlog/')
def userlog():
    return render_template('home/userlog.html')

@home.route('/moviecollect/')
def moviecollect():
    return render_template('home/moviecollect.html')

@home.route("/indexbanner/")
def indexbanner():
    return render_template('home/indexbanner.html')

@home.route('/search/')
def search():
    return render_template('home/search.html')

@home.route('/play/')
def play():
    return render_template('home/play.html')
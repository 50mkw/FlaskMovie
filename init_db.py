from app import db
import datetime
from app.models import *

if __name__ == '__main__':
    # 创建数据表
    # db.create_all()

    # 添加角色
    role = Role(
        name="超级管理员",
        auths="",
    )
    db.session.add(role)
    db.session.commit()

    # 添加管理员
    from werkzeug.security import generate_password_hash

    admin = Admin(
        name='admin',
        pwd=generate_password_hash('flaskadmin'),  # 加密密码
        is_super=0,
        role_id=1,
    )
    db.session.add(admin)
    db.session.commit()

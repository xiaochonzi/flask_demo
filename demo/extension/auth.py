# -*- coding:utf-8 -*-
from flask_jwt import JWT, jwt_required
from demo.orm.models import User


class Auth(object):
    def error_handle(self, e):
        return e, 400

    def authenticate(self, username, password):
        userInfo = User.query.filter_by(username=username).first()
        if userInfo is None:
            self.error_handle("用户不存在")
        else:
            if password == userInfo.password:
                return userInfo
            else:
                self.error_handle("密码不正确")

    def identity(self, payload):
        id = payload['identity']
        return User.get_by_id(id)

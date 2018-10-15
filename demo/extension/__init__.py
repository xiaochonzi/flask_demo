# -*- coding:utf-8 -*-
from flask_cors import CORS
from flask_mail import Mail
from flask_socketio import SocketIO
from flask_jwt import JWT
from .celery import CeleryExt
from .auth import Auth

cors = CORS()
mail = Mail()
socketio = SocketIO()
celeryext = CeleryExt()
auth = Auth()
jwt = JWT(authentication_handler=auth.authenticate, identity_handler=auth.identity)

from demo.orm import db

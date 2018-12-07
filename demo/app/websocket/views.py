# -*- coding:utf-8 -*-
from flask import request
from flask_socketio import send, emit, disconnect
from flask_login import current_user
from flask_jwt import jwt_required

from demo.extension import socketio


@socketio.on('client_event')
def client_msg(msg):
    print(request.headers)


@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})

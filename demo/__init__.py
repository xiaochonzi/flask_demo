# -*- coding:utf-8 -*-
from flask import Flask

from demo.config import config
from demo.orm import db
from demo.extension import celeryext,cors,socketio,jwt
from demo import schedule


def create_app(config_name):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    init_app(app)
    init_task(app)
    register_blueprint(app)
    return app


def init_app(app):
    db.init_app(app)
    cors.init_app(app)
    socketio.init_app(app)
    celeryext.init_app(app)
    jwt.init_app(app)
    schedule.run_continuously(1)


def register_blueprint(app):
    from demo.app.main import bp
    app.register_blueprint(bp)

    from demo.app.websocket import bp
    # app.register_blueprint(bp)


def init_task(app):
    def sendMsg():
        socketio.emit("thread_event", {"data": "test"})

    schedule.every(5).seconds.do(sendMsg)

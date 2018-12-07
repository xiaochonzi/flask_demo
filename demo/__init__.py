# -*- coding:utf-8 -*-
from flask import Flask

from demo import schedule
from demo.orm import db
from demo.config import config
from demo.extension import celeryext, cors, socketio, jwt


def create_app(config_name):
    """创建application

    :param config_name:
    :return:
    """
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_app(app)
    register_task(app)
    register_filter(app)
    register_blueprint(app)
    register_trigger(app)
    register_singal(app)
    return app


def register_app(app):
    """注册组件

    :param app:
    :return:
    """
    db.init_app(app)
    cors.init_app(app)
    socketio.init_app(app)
    celeryext.init_app(app)
    jwt.init_app(app)
    schedule.run_continuously(1)


def register_task(app):
    """注册定时任务

    :param app:
    :return:
    """

    def test_send_message():
        socketio.emit("thread_event", {"data": "test"})

    schedule.every(5).seconds.do(test_send_message)


def register_filter(app):
    """注册拦截器

    :param app:
    :return:
    """
    pass


def register_blueprint(app):
    """ 注册视图

    :param app:
    :return:
    """
    from demo.app.main import bp
    app.register_blueprint(bp)

    from demo.app.websocket import bp
    app.register_blueprint(bp)


def register_trigger(app):
    """注册触发器

    :param app:
    :return:
    """
    from demo.triggers import start_trigger
    start_trigger.init_app(app)


def register_singal(app):
    """注册信号

    :param app:
    :return:
    """
    from demo.singals import on_start
    on_start.send(app)

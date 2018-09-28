# -*- coding:utf-8 -*-
from flask import Flask

from demo.config import config
from demo.orm import db
from demo.extension import celeryext


def create_app(config_name):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    init_app(app)
    register_blueprint(app)
    return app


def init_app(app):
    db.init_app(app)
    celeryext.init_app(app)


def register_blueprint(app):
    from demo.app.main import bp
    app.register_blueprint(bp)

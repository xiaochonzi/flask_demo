# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(24)
    TEMPLATES_AUTO_RELOAD = True
    CSRF_ENABLED = True
    UPLOAD_FOLDER = os.path.join(basedir, 'static/uploads/')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:lua12378900@10.0.0.64:43306/violet?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 1000  # 默认 pool_size=5
    SQLALCHEMY_POOL_TIMEOUT = 10  # 默认 10秒
    SQLALCHEMY_POOL_RECYCLE = 500  # 配置要小于 数据库配置 wait_timeout
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_RECORD_QUERIES = True

    CORS_MAX_AGE = 3600
    CORS_SUPPORTS_CREDENTIALS = True
    BROKER_URL = 'redis://10.0.0.64:6379/1'
    CELERY_RESULT_BACKEND = 'redis://10.0.0.64:6379/1'



    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    @staticmethod
    def init_app(app):
        Config.init_app(app)


config = {
    "develop": DevelopConfig
}

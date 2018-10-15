# -*- coding:utf-8 -*-
from celery import Celery


class CeleryExt(object):
    a = set()
    celery = Celery(__name__)

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.celery.conf.update(app.config)
        TaskBase = self.celery.Task

        class ContextTask(TaskBase):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        self.celery.Task = ContextTask
        return self.celery



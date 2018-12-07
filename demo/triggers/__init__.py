# -*- coding:utf-8 -*-
from demo.singals import on_start


class OnStartTrigger(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        on_start.connect(self.trigger, app)

    def trigger(self, *extra):
        print(extra)


start_trigger = OnStartTrigger()

# -*- coding:utf-8 -*-
from flask.signals import Namespace

_signals = Namespace()

on_start = _signals.signal('on_start')

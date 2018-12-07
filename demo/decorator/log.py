# -*- coding:utf-8 -*-
from functools import wraps

from flask import request


def log():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            values = request.values.copy()
            json = request.json
            print('log', values, json)
            try:
                rv = func(*args, **kwargs)
                return rv
            except Exception as e:
                raise e

        return wrapper

    return decorator

# -*- coding:utf-8 -*-
from demo import create_app, celeryext

app = create_app('develop')
celery = celeryext.celery

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer

    server = WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()

# -*- coding:utf-8 -*-
from demo import create_app, celeryext

app = create_app('develop')
celery = celeryext.celery

if __name__ == '__main__':
    from geventwebsocket import WebSocketServer
    server = WebSocketServer(('0.0.0.0', 5000), app)
    server.serve_forever()
    # socketio.run(app, port=5000)

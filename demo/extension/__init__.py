# -*- coding:utf-8 -*-
from flask_mail import Mail

from .celery import CeleryExt

mail = Mail()
celeryext = CeleryExt()



from demo.orm import db
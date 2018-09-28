# -*- coding:utf-8 -*-
from flask import current_app

from demo.extension import celeryext, mail

celery = celeryext.celery


@celery.task
def _send_async_email(msg):
    print(msg)


def send_mail(msg):
    _send_async_email.delay(msg)

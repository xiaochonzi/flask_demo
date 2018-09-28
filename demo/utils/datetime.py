# -*- coding:utf-8 -*-
from datetime import datetime, timedelta


def date_format(s, fmt):
    t = datetime.strptime(s, fmt)
    return int(t.timestamp())



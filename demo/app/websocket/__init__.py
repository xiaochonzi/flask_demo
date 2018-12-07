# -*- coding:utf-8 -*-
from flask import Blueprint

bp = Blueprint("websocket", __name__)

from . import views

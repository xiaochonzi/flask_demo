# -*- coding:utf-8 -*-
import os
import time
from flask import current_app
from werkzeug.utils import secure_filename

from .tale import md5, random_str

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def md5_file(fp):
    if isinstance(fp, (str, bytes, bytearray)):
        fdata = fp
    elif hasattr(fp, 'read'):
        fdata = fp.read()
    elif fp is None:
        return None
    else:
        fdata = fp
    return md5(fdata)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(file):
    if file and allowed_file(file.filename):
        origin_name = secure_filename(file.filename)
        new_name = str(int(time.time())) + random_str(4) + origin_name[origin_name.rindex("."):]
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], new_name))
        return new_name

# -*- coding:utf-8 -*-
from flask import request, jsonify, make_response, render_template
from sqlalchemy.sql import and_, label

from . import bp
from demo.orm.models import *
from demo.decorator.log import log
from demo.utils.captcha import Captcha
from demo.utils.file import upload_file
from demo.task.mail import send_mail as task_send_mail


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/robots.txt")
def robot():
    return render_template('robots.txt')


@bp.route("/list")
def log_list():
    resp = dict()
    try:
        note = request.values.get("note", default="成功", type=str)
        startTime = request.values.get("startTime", type=int)
        endTime = request.values.get("endTime", type=int)
        pageNo = request.values.get('pageNo', default=1, type=int)
        pageSize = request.values.get("pageSize", default=20, type=int)
        sortName = request.values.get("sortName", default="time")
        sortOrder = request.values.get("sortOrder", default="desc")
        filters = [and_(1 == 1)]
        if note:
            filters.append(and_(SpiderLog.note.like('%{}%'.format(note))))
        if startTime:
            filters.append(and_(SpiderLog.time > startTime))
        if endTime:
            filters.append(and_(SpiderLog.time < endTime))
        sort_by = ''
        column = SpiderLog.get_column_by_name(sortName)
        if column:
            sort_by = '%s %s' % (column.name, sortOrder)
        pagination = SpiderLog.query.filter(*filters).order_by(sort_by).paginate(pageNo, per_page=pageSize,
                                                                                 error_out=False)
        resp['page'] = {
            "pageNo": pagination.page,
            "totalPages": pagination.pages,
            "pageSize": pagination.per_page,
            "totalRows": pagination.total,
            "hasNext": pagination.has_next,
            "hasPrev": pagination.has_prev,
            "prevNum": pagination.prev_num,
            "nextNum": pagination.next_num
        }
        resp['list'] = [item.to_json() for item in pagination.items]
        resp['result'] = 1
    except Exception as e:
        print(e)
        resp['result'] = 0
    return jsonify(resp)


@bp.route("/captcha")
def captcha():
    obj = Captcha()
    img, code = obj.generate_verification_code()
    resp = make_response(img)
    resp.headers['Content-Type'] = 'image/jpeg'
    return resp


@bp.route("/sendmail")
def send_mail():
    task_send_mail("send_mail")
    return jsonify({"result": 1})


@bp.route("/upload", methods=['GET', 'POST'])
def upload():
    files = request.files
    file = files['file']
    filename = upload_file(file)
    return jsonify({"result": filename})


@bp.route("/log", methods=['GET', 'POST'])
@log()
def log():
    values = request.values
    json = request.json
    print(values, json)
    return jsonify({"result": 1})

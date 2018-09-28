# -*- coding:utf-8 -*-
from datetime import datetime

from . import db


def now():
    return int(datetime.now().timestamp())


class ModelMixin(object):
    @classmethod
    def get_by__id(cls, id):
        if id:
            return cls.query.get(id)
        else:
            return None

    def save(self):
        db.session.add(self)
        return self

    def delete(self):
        db.session.delete(self)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    @classmethod
    def update(cls, **kwargs):
        try:
            id = kwargs.get('id', None)
            obj = cls.get_by_id(id)
            if obj:
                for field, value in kwargs.items():
                    setattr(obj, field, value)
            else:
                obj = cls.create(**kwargs)
            return obj
        except Exception:
            return None

    @classmethod
    def get_column_by_name(cls, name):
        try:
            return cls.__dict__[name]
        except Exception:
            pass
        return None

    @staticmethod
    def page(pagination):
        return {
            "pageNo": pagination.page,
            "totalPages": pagination.pages,
            "pageSize": pagination.per_page,
            "totalRows": pagination.total,
        }


class SpiderLog(ModelMixin, db.Model):
    __tablename__ = "spider_log"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    time = db.Column("time", db.Integer)
    type = db.Column("type", db.String(128))
    note = db.Column("note", db.Text)
    spiderId = db.Column("spider_id", db.String(128))
    proxyUid = db.Column("proxy_uid", db.String(255))
    containerId = db.Column("container_id", db.String(255))

    def __init__(self, *args, **kwargs):
        super(SpiderLog, self).__init__(*args, **kwargs)

    def to_json(self):
        return {
            "id": self.id,
            "time": self.time,
            "type": self.type,
            "note": self.note,
            "spiderId": self.spiderId,
            "proxyUid": self.proxyUid,
            "containerId": self.containerId
        }

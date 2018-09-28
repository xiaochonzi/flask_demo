# -*- coding:utf-8 -*-
import six
import hashlib
import random
import string


def to_unicode(text, encoding=None, errors='strict'):
    if isinstance(text, six.text_type):
        return text
    if not isinstance(text, (bytes, six.string_types)):
        raise TypeError('to_unicode must receive a bytes,str or unicode')
    if encoding is None:
        encoding = 'utf-8'
    return text.decode(encoding, errors)


def to_bytes(text, encoding=None, errors='strict'):
    if isinstance(text, bytes):
        return text
    if not isinstance(text, (bytes, six.string_types)):
        raise TypeError('to_bytes must receive a bytes,str or unicode')
    if encoding is None:
        encoding = 'utf-8'
    return text.encode(encoding, errors)


def md5(text):
    s = to_bytes(text)
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()


def random_str(num):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
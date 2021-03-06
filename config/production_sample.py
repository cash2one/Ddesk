# -*- coding: utf-8 -*-
from .default import Config


class ProductionConfig(Config):
    # Flask
    DEBUG = True
    SECRET_KEY = ''

    # Mysql(SQLalchemy)
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # UPYUN
    UPYUN_BUCKET = ''
    UPYUN_USERNAME = ''
    UPYUN_PASSWORD = ''
    UPYUN_DOMAIN = ''

    # Other
    LOGIN_TOKEN = ''

    # SMS API
    TAOBAO_API_KEY = ''
    TAOBAO_API_SECRET = ''
    DINGTALK_API_CID = ''
    DINGTALK_API_SECRET = ''
    DINGTALK_API_MSGID = ''
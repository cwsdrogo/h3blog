# -*- coding: utf-8 -*-
import os
import sys
import hashlib

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or hashlib.new(name='md5', string='h3blog python@#').hexdigest()

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = True

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('H3BLOG Admin', MAIL_USERNAME)

    H3BLOG_EMAIL = os.getenv('H3BLOG_EMAIL')
    H3BLOG_POST_PER_PAGE = 10
    H3BLOG_MANAGE_POST_PER_PAGE = 15
    H3BLOG_COMMENT_PER_PAGE = 15
    H3BLOG_SLOW_QUERY_THRESHOLD = 1

    H3BLOG_UPLOAD_TYPE = 'qiniu' # 默认本地上传
    H3BLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    H3BLOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

    MAX_CONTENT_LENGTH = 32 * 1024 * 1024

    QINIU_CDN_URL = os.getenv('QINIU_CDN_URL','http://cdn.h3blog.com/')
    QINIU_ACCESS_KEY = os.getenv('QINIU_ACCESS_KEY','LlO13INj1pl5Ow5WtoJF0FOcoFKpCbGRXEiPRSV9')
    QINIU_SECRET_KEY = os.getenv('QINIU_SECRET_KEY','N2j2dgnvncu3DSUyM_-_4WerDJOKahefJTrJAkje')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

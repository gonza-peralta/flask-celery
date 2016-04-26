'''
Created on Apr 25, 2016

@author: gonzalo
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    @staticmethod
    def init_app(app):
        pass


class LocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///" + os.path.join(basedir,
                                                           "data-dev.sqlite")
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'


config = {
    "local": LocalConfig}

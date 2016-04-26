'''
Created on Apr 25, 2016

@author: gonzalo
'''

from extensions import db
from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    # Register the blueprints
    from appblueprint.views import externalmodule
    app.register_blueprint(externalmodule, url_prefix='/externalmodule')
    return app

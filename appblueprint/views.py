'''
Created on Apr 26, 2016

@author: gonzalo
'''
from flask import Blueprint
import json

externalmodule = Blueprint('externalmodule', 'externalmodule')


@externalmodule.route('/')
def index():
    return json.dumps({"success": True})

'''
Created on Apr 25, 2016

@author: gonzalo
'''
from factory import create_app
from model import User
from extensions import db

if __name__ == '__main__':
    app = create_app("local")
    db.create_all(app=app)

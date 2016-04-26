'''
Created on Apr 25, 2016

@author: gonzalo
'''
from app.factory import create_app

from factory import make_celery
from app.model import User
from app.extensions import db
import json

app = create_app("local")
celery = make_celery(app)


@celery.task(name="changename")
def changename():
    user = User.query.filter_by(name="John").first()
    user.surname = "Doe"
    try:
        db.session.add(user)
        db.session.commit()
    except Exception, ex:
        db.session.rollback()
        raise ex
    return json.dumps(user.to_json())

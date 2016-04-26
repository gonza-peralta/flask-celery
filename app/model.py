'''
Created on Apr 25, 2016

@author: gonzalo
'''
from extensions import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(72), nullable=False)
    surname = db.Column(db.String(72), nullable=False)

    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "surname": self.surname}

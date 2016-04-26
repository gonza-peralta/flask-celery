'''
Created on Apr 25, 2016

@author: gonzalo
'''
from app.factory import create_app
from extensions import db

app = create_app("local")

from model import User
import json


@app.route('/user', methods=['POST'])
def create():
    user = User(name="John", surname="Connor")
    try:
        db.session.add(user)
        db.session.commit()
    except Exception, ex:
        db.session.rollback()
        raise ex
    return json.dumps(user.to_json())


@app.route('/user', methods=['PUT'])
def change():
    user = User.query.filter_by(name="John").first()
    user.surname = "Lewis"
    try:
        db.session.add(user)
        db.session.commit()
    except Exception, ex:
        db.session.rollback()
        raise ex
    return json.dumps(user.to_json())


@app.route('/user', methods=['GET'])
def get():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(user.to_json())
    return json.dumps(users_list)

def main():
    print app.url_map
    app.run(debug=True)

if __name__ == "__main__":
    main()


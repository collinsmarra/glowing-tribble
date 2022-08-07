from flask import Blueprint, current_app, request,session
from api.app import db
from api.models import Users, Posts

users = Blueprint('users', __name__)

@users.route("/new", methods=['POST'])
def new():
    username = request.json['username']
    age = request.json['age']
    user = Users(username=username, age=age)
    db.session.add(user)
    db.session.commit()
    user = db.session.scalar(
        Users.select().filter_by(username=username))
    return {"username": user.username, "age": user.age}, 201

@users.route("/posts/<int:id>/hasliked", methods=['GET'])
def has_liked(id):
   user = session.get('username')
   post = db.session.scalar(
       Posts.select().filter_by(id=id))
   return user.has_liked_post(post)

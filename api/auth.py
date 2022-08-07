from flask import Blueprint, request, session, abort
from api.models import Users
from api.app import db

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    session['username'] = username
    user = db.session.scalar(
        Users.select().filter_by(
            username=username))
    if not username:
        abort(404)
    return {"username": user.username, "age": user.age}, 200


@auth.route("/logout", methods=["POST"])
def logout():
    username = session.get('username')
    if not username:
        abort(400)
    session['username'] = None
    return "", 204

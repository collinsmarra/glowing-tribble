from flask import current_app, request, jsonify, Blueprint, session,jsonify
import sqlalchemy as sqla
from api.app import db
from api.models import Users, Posts

posts = Blueprint('posts', __name__)


@posts.route("/new", methods=["POST"])
def new(args):
    post = Posts(**args)
    db.session.add(house)
    db.session.commit()
    return "", 201


@posts.route("/posts/<int:id>/delete", methods=["DELETE"])
def delete(id):
    post = db.session.scalar(
        Posts.select().filter_by(id=id))
    db.session.delete(post)
    db.session.commit()
    return "", 204


@posts.route("/posts/<int:id>/like", methods=["GET"])
def like(id):
    username = session.get('username')
    user = db.session.scalar(
        Users.select().filter_by(username = username))
    post = db.session.scalar(
        Posts.select().filter_by(id=id))
    user.likec_post(post)
    db.session.commit()
    return jsonify(f"<Post {post.id}>")


@posts.route("/posts/<int:id>/unlike", methods=["GET"])
def unlike():
    username = session.get('username')
    user = db.session.scalar(
        Users.select().filter_by(username = username))
    post = db.session.scalar(
        Posts.select().filter_by(id=id))
    user.unlike_post(post)
    db.session.commit()
    return jsonify(f"<Post {post.id}>")


@posts.route("/posts/<int:id>/likes", methods=["GET"])
def likes(id):
    post = db.session.scalar(
        Posts.select().filter_by(
            id = id))
    data = {"likes": post.likes.count()}
    return  jsonify(data)

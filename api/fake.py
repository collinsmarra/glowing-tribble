import random
import click
from flask import Blueprint
from faker import Faker
from api.app import db
from api.models import Users, Posts

fake = Blueprint('fake', __name__)
faker = Faker()


@fake.cli.command()
@click.argument('num', type=int)
def users(num):
    """
        Generate a given number of users
    """
    users = []
    for i in range(num):
        user = Users(username=faker.user_name(), age=faker.numerify())
        db.session.add(user)
        users.append(user)

    db.session.commit()
    print(num, ' Users added.')


@fake.cli.command()
@click.argument('num', type=int)
def posts(num):
    """
        Generate fake posts
    """
    users = db.session.scalars(Users.select()).all()
    for i in range(num):
        user = random.choice(users)
        post = Posts(author=user.id,  body=faker.paragraph())
        db.session.add(post)
    db.session.commit()
    print( num, ' Posts added.' )


@fake.cli.command()
@click.argument('num', type=int)
def likes(num):
    """
        Generate likes
    """
    users = db.session.scalars(Users.select()).all()
    posts = db.session.scalars(Posts.select()).all()
    for i in range(num):
        user = random.choice(users)
        post = random.choice(posts)
        user.likec_post(post)
    db.session.commit()
    print(num, ' Total likes generate.')


@fake.cli.command()
@click.argument('num', type=int)
def liked(num):
    """
        See how many users liked
    """
    posts = db.session.scalars(Posts.select()).all()
    for i in range(num):
        post = random.choice(posts)
        if post.likes.count():
            data = {f"<Post {post.id}>": f"likes {post.likes.count()}"}
            print(data)

"""
    print the user.id(s) if the users who have liked a post
"""


@fake.cli.command()
def user_likes():
    """
        check the posts that the user has liked
    """
    users = db.session.scalars(Users.select()).all()
    posts = db.session.scalars(Posts.select()).all()
    for post in posts:
        for user in users:
            if user.has_liked_post(post):
                data = {f"<{user.username}>": f"<{post.id}>"}
                print(data)


@fake.cli.command()
@click.argument('num', type=int)
def all_posts(num):
    """
        Print all posts liked by a user
    """
    user = db.session.scalar(Users.select().filter_by(id=num))
    posts = db.session.scalars(Posts.select()).all()
    count = 0
    for post in posts:
        if user.has_liked_post(post):
            print(f"<Post {post.id}>")
            count += 1
    data = {f"<User {user.id}>": f"likes {count} posts"}
    print(data)

import sqlalchemy as sqla
import sqlalchemy.orm as sqla_orm
from api.app import db


class Updateable:
    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)


class Users(db.Model):
    __tablename__ = 'users'
    id = sqla.Column(sqla.Integer, primary_key=True)
    username = sqla.Column(sqla.String, nullable=False, unique=True)
    age = sqla.Column(sqla.Integer, nullable=False)
    liked = sqla_orm.relationship(
        'PostLike',
        foreign_keys='PostLike.user_id',
        backref='username', lazy='dynamic'
    )

    def __repr__(self):
        return f"<User {self.username}>"

    def likec_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id=self.id, post_id=post.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            with db.begin() as session:
                like = session.scalar(
                    PostLike.select().filter_by(
                        user_id=self.id, post_id=post.id
                    )
                )
                session.delete(like)
                session.commit()
                
    def has_liked_post(self, post):
        qry = sqla.select([sqla.func.count()]).select_from(
            PostLike).where(PostLike.user_id==self.id,
                         PostLike.post_id == post.id)
        vv = db.session.execute(qry)
        return vv.first()[0]

    def likes(self):
        """
            generate the posts that the user likes
        """
        res = []
        posts = db.session.scalars(Posts.select()).all()
        for post in posts:
            if user.has_liked_post(post):
                res.append(post)
        print([f"<Post {post.id}>" for post in posts])


class Posts(db.Model):
    __tablename__ = "posts"
    id = sqla.Column(sqla.Integer, primary_key=True)
    author = sqla.Column(sqla.Integer, sqla.ForeignKey(Users.username))
    body = sqla.Column(sqla.Text)
    likes = sqla_orm.relationship(
        'PostLike', backref='post', lazy='dynamic')

    def __repr__(self):
        return f"<Post {self.author}>"


class PostLike(db.Model):

    __tablename__ = "post_like"
    id = sqla.Column(sqla.Integer, primary_key=True)
    user_id = sqla.Column(sqla.Integer, sqla.ForeignKey(Users.id))
    post_id = sqla.Column(sqla.Integer, sqla.ForeignKey(Posts.id))


db.create_all()

from flask import Flask, request
from alchemical.flask import Alchemical
import sqlalchemy as sqla
from config import ConfigClass

db = Alchemical()

def create_app(config_class=ConfigClass):
    app = Flask(__name__)

    app.config.from_object(config_class)
    db.init_app(app)

    from api.users import users
    app.register_blueprint(users, url_prefix="/users")

    from api.auth import auth
    app.register_blueprint(auth)

    from api.posts import posts
    app.register_blueprint(posts, url_prefix="/posts")

    from api.fake import fake
    app.register_blueprint(fake)

    from api import models

    @app.shell_context_processor
    def shell_context():
        ctx = {'db': db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(models, '__bases__') and \
                    db.Model in getattr(model, '__bases__'):
                ctx[attr] = model
        return ctx

    @app.after_request
    def after_request(response):
        request.get_data()
        return response

    return app

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigClass:
    SECRET_KEY = os.urandom(32).hex()
    ALCHEMICAL_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

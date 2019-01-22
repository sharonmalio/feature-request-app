import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '@Rocky#123.!'
    SQLALCHEMY_ECHO = True
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or \
    'postgresql:///' + os.path.join(basedir, 'featureapp')
=======
    SQLALCHEMY_DATABASE_URI = "postgresql:///featureapp"
>>>>>>> dd26e2fe2351cd257945d6f939cd3ca61d34a7aa
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


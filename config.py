import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '@Rocky#123.!'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@Rocky#123.@localhost:3306/featureapp'

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


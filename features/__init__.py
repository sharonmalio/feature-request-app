import os
from flask_login import LoginManager
from config import basedir
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


login.login_view = 'login'

from features import routes, models, tables

if __name__=='__main__':
    app.run(debug=True)


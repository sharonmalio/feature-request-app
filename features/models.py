from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from datetime import date
from features import db, login
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSON


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    features = db.relationship('Feature', backref='filledby', lazy='dynamic')

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    features = db.relationship('Feature', backref='ownedby', lazy='dynamic')

    def __repr__(self):
        return "<Client: {}>".format(self.name)


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=False)
    description = db.Column(db.String(120), index=True, unique=False)
    client = db.Column(db.String(128), index=True, unique=False)
    client_priority = db.Column(db.Integer, index=True, unique=False)
    target_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    product_area = db.Column(db.String(65), unique=False, index=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

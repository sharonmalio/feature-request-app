from datetime import datetime
from datetime import date
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    features = db.relationship('Feature', backref='filledby', lazy='dynamic')

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
    def __repr__(self):
        return '<User {}>'.format(self.username)  
      
class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=False)
    description = db.Column(db.String(120), index=True, unique=False)
    client = db.Column(db.String(128), index=True, unique=False) 
    client_priority = db.Column(db.Integer, index=True, unique=False)
    target_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    product_area = db.Column(db.String(65), unique=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

from .db import db, ActiveModel
from flask.ext.login import UserMixin, AnonymousUserMixin
from flask.ext.bcrypt import check_password_hash, generate_password_hash

class User(db.Model, ActiveModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    active = db.Column(db.Boolean(), default=True, server_default='1')

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
        self.active = True

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(username=username).first()
        return user if user and check_password_hash(user.password, password) else None
    
    def __repr__(self):
        return '<User %r>' % self.username

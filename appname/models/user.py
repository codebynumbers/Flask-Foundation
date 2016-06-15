from flask_login import UserMixin, AnonymousUserMixin
from flask_bcrypt import check_password_hash, generate_password_hash

from .db import db, ActiveModel


class User(UserMixin, ActiveModel, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    active = db.Column(db.Boolean(), default=True, server_default='1')

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
        self.active = True

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def update_password(self, password):
        self.password = generate_password_hash(password)
        
    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(username=username).first()
        return user if user and check_password_hash(user.password, password) else None
    
    def __repr__(self):
        return '<User %r>' % self.username

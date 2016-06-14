from db import db, ActiveModel


class Widget(ActiveModel, db.Model):
    __tablename__ = "widgets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", backref="widgets")
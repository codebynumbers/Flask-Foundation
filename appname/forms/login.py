from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms import validators


class LoginForm(Form):
    username = StringField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.optional()])

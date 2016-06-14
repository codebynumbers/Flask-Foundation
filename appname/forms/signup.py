from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms import validators


class SignupForm(Form):
    username = StringField(u'Email', validators=[validators.required()])
    password = PasswordField(
        u'Password', validators=[validators.required(), validators.Length(min=8)])
    password_confirm = PasswordField(
        u'Repeat Password', validators=[validators.required(), validators.EqualTo('password')])

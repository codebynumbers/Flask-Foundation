from flask_wtf import Form
from wtforms import PasswordField
from wtforms import validators


class ChangePasswordForm(Form):
    current_password = PasswordField(
        u'Current Password', validators=[validators.required()])
    password = PasswordField(
        u'New Password', validators=[validators.required(), validators.Length(min=8)])
    password_confirm = PasswordField(
        u'Repeat New Password', validators=[validators.required(), validators.EqualTo('password')])

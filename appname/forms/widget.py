from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class WidgetForm(Form):
    name = StringField(u'Name', validators=[DataRequired()])
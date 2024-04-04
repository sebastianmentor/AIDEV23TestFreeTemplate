from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    phone = StringField('Phone', [DataRequired()])
    message = TextAreaField('Message', [DataRequired()])
    submit = SubmitField('Send')
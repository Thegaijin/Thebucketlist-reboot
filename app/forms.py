# /app/forms.py

from flask import wtforms
from wtforms import (Form, TextField, TextAreaField,
                     validators, StringField, SubmitField, PasswordField)


class SignUpForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('New Password', [validators.Required()])
    submit = SubmitField('Log in')

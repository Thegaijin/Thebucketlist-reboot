# /app/forms.py

from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from flask import flash
from flask_wtf import FlaskForm
from wtforms import (validators, StringField,
                     SubmitField, PasswordField, ValidationError)
from wtforms.validators import DataRequired, EqualTo

user = BucketlistApp()


class SignUpForm(FlaskForm):
    """Form for users to create an account"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        """Method checks if username already exists"""

        username = field.data
        if username in user.users:
            flash('Username is already in use.')
            raise ValidationError('Username is already in use.')
        return True


class LoginForm(FlaskForm):
    """Form for users to log in"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

    def validate_usercredentials(self, field):
        """Method checks if username belongs to a user"""

        username = field.data
        if username not in user.users:
            flash('Username does not exist.')
            raise ValidationError('Username does not exist.')
        return True


class ListForm(FlaskForm):
    """Form for user to add lists"""

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add list')

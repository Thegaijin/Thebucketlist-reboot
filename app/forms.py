# /app/forms.py

from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from flask_wtf import FlaskForm
from wtforms import (validators, StringField,
                     SubmitField, PasswordField, ValidationError)
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    """Form for users to create an account"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate_username(self, username):
        """Method checks if username already exists"""

        username = self.username.data
        newuser = BucketlistApp()
        if username in newuser.usercredentials:
            raise ValidationError('Username is already in use.')
            return False
        return True


class LoginForm(FlaskForm):
    """Form for users to log in"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.newuser = BucketlistApp()

    def validate_username(self, username):
        """Method checks if username belongs to a user"""
        username = self.username.data

        if username not in self.newuser.usercredentials:
            return False
        return True

    ''' def validate_password(self, username, password):
        """Method checks if username belongs to a user"""
        username = self.username.data
        password = self.password.data

        if password != self.newuser.usercredentials[username]:
            return False
        return True
    '''

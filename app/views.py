# /app/views.py
from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from app import login_manager 
from .forms import SignUpForm, LoginForm
from flask import (Flask, flash, redirect,
                   render_template, request, session, url_for)
from flask_login import login_required, login_user, logout_user

from passlib.hash import sha256_crypt


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                           title='The')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = sha256_crypt.encrypt((str(form.password.data)))
        confirmpassword = sha256_crypt.encrypt((str(form.confirmpassword.data)))
        new_user = User(username, password)
        BucketlistApp().signup(new_user)
        flash('Your account has been created')
        return redirect(url_for('login'))
    flash('Please enter your credentials as required and try again')
    return render_template('signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = sha256_crypt.encrypt((str(form.password.data)))
        user = BucketlistApp().login(username, password)
        if isinstance(user, User):
            login_user(user)

        next = flask.request.args.get('next')

        if not is_safe_url(next):
            return flask.abort(400)
        return redirect(next or url_for('lists'))
    else:
        flash('The username and password combination does not exist')
    return render_template('login.html', form=form)


@app.route('/lists', methods=["GET", "POST"])
@login_required
def lists():
    return render_template('lists.html')

@app.route('/logout')
@login_required
def logout():
    """Handle requests to the /logout route
    Log users out of the app
    """
    logout_user()
    flash('You have successfully been logged out.')
    # redirect to the login page
    return redirect(url_for('login'))

# Reload the user object from the user name stored in the session
# Stores the active user’s ID in the session
@login_manager.user_loader
def load_user(username):
    user = User(username)
    return user.get(username)
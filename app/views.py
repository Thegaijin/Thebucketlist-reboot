# /app/views.py
from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from app import login_manager
from .forms import SignUpForm, LoginForm, ListForm
from flask import (flash, redirect, render_template, request, session, url_for)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

user = BucketlistApp()
''' current_user = User() '''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                           title='The')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle requests to the /signup route

    Create a new user through the sign up form
    """

    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username not in user.users:
            # creating a user id
            if len(user.users) == 0:
                id = 1
            id = len(user.users) + 1

            # hashing the password
            pswd_hash = generate_password_hash(password)

            # creating instance of new_user
            new_user = User(id, username, pswd_hash)

        # add employee to the users dictionary and return True if done
        created = user.signup(new_user)
        flash('{}, Your account has been created'.format(username))

        if created:
            # redirect to the login page
            return redirect(url_for('login'))
        flash("User account was not created")

    # load sign up template
    return render_template('signup.html', form=form, title='Sign Up')


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle requests to the /login route

    Log a user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # return instance of current user
        loggedin = user.login(username, password)
        flash("Welcome, {}".format(loggedin.username))
        if isinstance(loggedin, User):
            flash("Now inside if statement")
            login_user(loggedin)
            flash("After login user")
            return redirect(url_for('view_lists'))

    # render the login template
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(username):
    """Loads user from the users dictionary"""
    flash("In user loader")
    return user.users.get(id)


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


@app.route('/view_lists', methods=["GET", "POST"])
# @login_required
def view_lists():
    """Render the lists template on the /lists route"""

    return render_template('lists.html', title="Lists")


@app.route('/add_list', methods=["GET", "POST"])
def add_list():
    """Render the list template on the /list route"""
    form = ListForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        new_list = user.users[username].create_list(name, description)
        flash(new_list)
        return redirect(url_for('view_lists'))

    return render_template('list.html', form=form, title="Lists")
# Reload the user object from the user name stored in the session
# Stores the active user’s ID in the session

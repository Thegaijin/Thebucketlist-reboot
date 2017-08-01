# /app/views.py
from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from app import login_manager
from .forms import SignUpForm, LoginForm, ListForm, ItemForm
from flask import (flash, redirect, render_template, request, session, url_for)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

user = BucketlistApp()
''' current_user = User() '''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


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
            return redirect(url_for('add_list'))

    # render the login template
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(username):
    """Loads user from the users dictionary"""
    flash("In user loader")
    return user.users.get(username)


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


@app.route('/add_list', methods=["GET", "POST"])
@login_required
def add_list():
    """Render the list template on the /add_list route"""

    add_list = True
    form = ListForm()
    if form.validate_on_submit():
        listname = form.name.data
        details = form.description.data
        if listname not in user.users[current_user.username].user_lists:
            # creating a user id
            if len(user.users[current_user.username].user_lists) == 0:
                id = 1
            id = len(user.users[current_user.username].user_lists) + 1

        all_lists = user.users[current_user.username].create_list(
            id, listname, details)
        list_objs = list(all_lists.values())
        flash(all_lists)
        flash(type(all_lists))
        flash(list_objs)

        return render_template('lists.html', form=form, action="Add", title="Add List", lists=list_objs)
    lists = user.users[current_user.username].user_lists
    list_objs = list(lists.values())
    return render_template('lists.html', form=form, action="Add", title="Lists", lists=list_objs)


@app.route('/edit_list/<listname>', methods=['GET', 'POST'])
@login_required
def edit_list(listname):
    """Enable functionality on the /edit_list route"""

    add_list = False
    the_list = user.users[current_user.username].view_list(listname)
    form = ListForm(obj=the_list)
    if form.validate_on_submit():
        name = form.name.data
        details = form.description.data

        all_lists = user.users[current_user.username].edit_list(
            name, details)
        list_objs = list(all_lists.values())

        return render_template('lists.html', form=form, action="Edit", title="Edit List", lists=list_objs)
    flash("Edit the {} list".format(listname))
    return render_template('lists.html', form=form, action="Edit", title="Edit List")


@app.route('/delete_list/<listname>', methods=['GET', 'POST'])
@login_required
def delete_list(listname):
    """Enable the delete functionality on the delete_list route

    Key Arguments:
    listname -- Name of list to be deleted
    """
    # the_list = user.users[current_user.username].user_lists[listname]
    form = ListForm()
    all_lists = user.users[current_user.username].delete_list(listname)
    list_objs = list(all_lists.values())

    return render_template('lists.html', form=form, title="Lists", lists=list_objs)


@app.route('/view_list/<listname>', methods=['GET', 'POST'])
@login_required
def view_list(listname):
    """Renders the items template to display items in list

    Key Arguments:
    listname -- Name of list to be viewed
    """
    the_list = user.users[current_user.username].view_list(listname)
    form = ItemForm()
    if form.validate_on_submit():
        name = form.name.data
        items = user.users[current_user.username].add_item(listname, name)
    items = the_list.items

    return render_template('items.html', title='Items', form=form,
                           items=items, listname=listname)


@app.route('/edit_item/<listname>/<itemname>', methods=['GET', 'POST'])
@login_required
def edit_item(listname, itemname):
    the_items = user.users[current_user.username].view_items(listname)
    the_item = user.users[current_user.username].view_item(listname, itemname)
    form = ItemForm(obj=the_item)
    if form.validate_on_submit():
        name = form.name.data

        # Applying changes to item
        items = user.users[current_user.username].update_item(
            listname, itemname, name)
        flash("Changes")
        return redirect(url_for('view_list', listname=listname))
    flash("Edit the {} item in the {} list".format(itemname, listname))
    return render_template('items.html', title='Items', form=form,
                           items=the_items, listname=listname)


@app.route('/delete_item/<listname>/<itemname>', methods=['GET', 'POST'])
@login_required
def delete_item(listname, itemname):
    items = user.users[current_user.username].delete_item(
        listname, itemname)
    form = ListForm()
    return render_template('items.html', title='Items', form=form,
                           items=items, listname=listname)

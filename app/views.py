# /app/views.py
from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from flask import (Flask, flash, redirect,
                   render_template, request, session, url_for)
from forms import SignUpForm
from passlib.hash import sha256_crypt


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='The')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm(request.form)
    if request.method == "POST" and form.validate:
        username = form.username.data
        password = sha256_crypt.encrypt((str(form.password.data)))
        BucketlistApp.signup(username, password)
        flash('Your account has been created')
        return redirect(url_for('login'))
    flash('Please enter your credentials as required and try again')
    return render_template('signup.html', form=form)

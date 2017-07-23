# /app/views.py
from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from flask import (Flask, flash, redirect, render_template,
                   request, session, url_for)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='The')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

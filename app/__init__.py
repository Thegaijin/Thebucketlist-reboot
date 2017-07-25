# /app/__init__.py

from flask import Flask
from flask_login import LoginManager

# variable app assigned an instance of class flask
app = Flask(__name__)
app.config.from_object('config')
# variable login_manager assigned an instance of class LoginManager
login_manager = LoginManager()

# For user session management and remember the users’ session
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"


# import at the end to avoid circular reference
from app import views

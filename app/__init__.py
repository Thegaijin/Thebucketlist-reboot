# /app/__init__.py

from flask import Flask
from flask_login import LoginManager

# variable app assigned an instance of class flask
app = Flask(__name__)

# variable login_manager assigned an instance of class LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# import at the end to avoid circular reference
from app import views
# /app/models/bucketlistApp.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .users import User


class BucketlistApp(object):
    """BucketlistApp class handles user registration,
    sign in and sign out
    """

    def __init__(self):
        self.users = {}
        self.usercredentials = {}
        self.loggedin = []

    def signup(self, username, password):
        """method to save users on sign up

        Keyword Arguments:
        username -- New users username
        password -- New users password
        """
        # hashing the password
        pswd_hash = generate_password_hash(password)

        # creating instance of new_user
        new_user = User(username, pswd_hash)

        # add the instance of User to the users dictionary and add the
        # username as a key and password as value to usercredentials
        self.users[new_user.username] = new_user
        self.usercredentials[username] = pswd_hash
        return True

    def login(self, username, password):
        """Method to login existing users

        Keyword Arguments:
        username -- The name the user signed up with
        password -- The password the user signed up with
        """
        # check if username exists
        if username in self.usercredentials:

            # check if password matches the value of the username key
            hashed_pswd = self.usercredentials[username]
            if check_password_hash(hashed_pswd, password) == True:

                # add username to loggedin users list
                self.loggedin.append(username)

                # return that users instance
                return self.users[username]
            return "The username and password combination \
                     does not exist"
        return "The username does not exist, please signup"

    def logout(self, username):
        """Method to logout a currently logged in user

        Keyword Arguments:
        username -- The name the user currently logged in
        """
        if username in self.loggedin:
            self.loggedin.remove(username)
            return self.loggedin
        return "The user was not logged out"


# CALLING THE FUNCTIONS: testing signup and login functionality
''' testuser = BucketlistApp()
print(testuser.signup('Thegaijin', '1234'))
print("**********************")
print(testuser.login("Thegaijin", "1234")) '''

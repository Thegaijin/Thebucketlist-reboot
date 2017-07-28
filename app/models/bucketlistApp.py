# /app/models/bucketlistApp.py


from .users import User
from flask_login import UserMixin, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


class BucketlistApp(object):
    """BucketlistApp class handles user registration,
    sign in and sign out
    """

    def __init__(self):
        self.users = {}

    def signup(self, new_user):
        """method to save users on sign up
        # FIXME: The keyword arguments
        Keyword Arguments:
        user -- New user object, an instance of the User class
        """
        ''' if username not in self.users:
            # creating a user id
            if len(self.users) == 0:
                id = 1
            id = len(self.users) + 1

            # hashing the password
            pswd_hash = generate_password_hash(password)

            # creating instance of new_user
            new_user = User(id, username, pswd_hash) '''

        # add username as a key and new_user instance
        # as value to users dictionary
        if isinstance(new_user, User):
            self.users[new_user.username] = new_user
            print("id: {}, username: {}, password: {}".format(
                new_user.id, new_user.username, new_user.pswd_hash))
            return True
        return 'User was not created'

    def login(self, username, password):
        """Method to login existing users

        Keyword Arguments:
        username -- The name the user signed up with
        password -- The password the user signed up with
        """
        # check if username exists
        if username in self.users:
            # check if password matches the value of the username key
            hashed_pswd = self.users[username].pswd_hash
            print(hashed_pswd)
            print(check_password_hash(hashed_pswd, password))
            if check_password_hash(hashed_pswd, password):
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
        return "The user was not logged out"


# CALLING THE FUNCTIONS: testing signup and login functionality
''' testuser = BucketlistApp()
pswd_hash = generate_password_hash("1234")
user = User(1, 'Thegaijin', pswd_hash)
print(testuser.signup(user))
print("**********************")
print(testuser.login("Thegaijin", "1234")) '''

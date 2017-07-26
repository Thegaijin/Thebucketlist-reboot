# /app/models/bucketlistApp.py

from .users import User


class BucketlistApp(object):
    """BucketlistApp class handles user registration,
    sign in and sign out
    """

    def __init__(self):
        self.users = {}
        self.usercredentials = {}
        self.loggedin = []

    def signup(self, new_user):
        """method to save users on sign up

        Keyword Arguments:
        username -- The name the user would like to use
        password -- The password the user would like to use
        confirmation_password -- Password to compare with above
        """
        self.users[new_user.username] = new_user
        self.usercredentials[new_user.username] = new_user.password
        return new_user

    # @classmethod
    def login(self, username, password):
        """Method to login existing users

        Keyword Arguments:
        username -- The name the user signed up with
        password -- The password the user signed up with
        """
        if username in self.usercredentials:
            if password == self.usercredentials[username]:
                self.loggedin.append(username)
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
new_user = User('Thegaijin', '1234')
testuser.signup(new_user)
print(testuser.login("Thegaijin", "1234")) '''

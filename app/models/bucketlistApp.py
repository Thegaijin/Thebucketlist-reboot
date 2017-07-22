class BucketlistApp(object):
    """BucketlistApp class handles user registration,
    sign in and sign out
    """

    def __init__(self):
        self.user_names = []
        self.users = {}
        self.loggedin = []

    def signup(self, username, password, confirmation_password):
        """method to save users on sign up

        Keyword Arguments:
        username -- The name the user would like to use
        password -- The password the user would like to use
        confirmation_password -- Password to compare with above
        """
        if username not in self.user_names:
            if password == confirmation_password:
                self.user_names.append(username)
                self.users[username] = password
                return self.user_names
            return "The password and confirmation password \
                    don't match"
        return "A user by that name already exists"

    def login(self, username, password):
        """Method to login existing users

        Keyword Arguments:
        username -- The name the user signed up with
        password -- The password the user signed up with
        """
        if username in self.users:
            if password == self.users[username]:
                self.loggedin.append(username)
                return self.users
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


# TODO: testing signup and login functionality

testuser = BucketlistApp()
testuser.signup("Thegaijin", "1234", "1234")
testuser.login("Thegaijin", "1234")
print(testuser.logout("Thegaijin"))

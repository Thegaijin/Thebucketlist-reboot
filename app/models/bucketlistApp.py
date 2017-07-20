class BucketlistApp(object):
    '''
    BucketlistApp class handles user registration,
    sign in and sign out
    '''

    def __init__(self):
        self.user_names = []
        self.users = {}
        self.loggedin = []

    def signup(self, username, password, confirmation_password):
        '''
        method to save users on sign up
        :param username:
        :param password:
        :param confirmation_password:
        '''
        if username not in self.user_names:
            if password == confirmation_password:
                self.user_names.append(username)
                self.users[username] = password
                return self.user_names
            return "The password and confirmation password \
                    don't match"
        return "A user by that name already exists"

    def login(self, username, password):
        '''
        Method to login existing users
        :param username:
        :param password:
        '''
        if username in self.users:
            if password == self.users[username]:
                self.loggedin.append(username)
                return self.users
            return "The username and password combination \
                     does not exist"
        return "The username does not exist, please signup"

    def logout(self, username):
        '''
        Method to logout a currently logged in user
        :param username:
        '''
        if username in self.loggedin:
            self.loggedin.remove(username)
            return self.loggedin
        return "The user was not logged out"


# TODO: testing signup and login functionality

testuser = BucketlistApp()
testuser.signup('Thegaijin', '1234', '1234')
testuser.login('Thegaijin', '1234')
print(testuser.logout('Thegaijin'))

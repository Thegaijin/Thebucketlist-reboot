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
        :param confirmation password:
        '''
        pass

    def login(self, username, password):
        '''
        Method to login existing users
        :param username:
        :param password:
        '''
        pass

    def logout(self, username):
        '''
        Method to logout a currently logged in user
        :param username:
        '''
        pass

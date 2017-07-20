import unittest
from app.models.bucketlistApp import BucketlistApp


class BucketlistAppTestCase(unittest.TestCase):
    '''
    Testing the functionality of the methods in 
    the BucketlistApp class
    '''

    def setUp(self):
        self.current = BucketlistApp()
        self.user_names = self.current.user_names
        self.test_dict = self.current.users
        self.loggedin = self.current.loggedin

    def test_bucketlistApp_instance(self):
        '''
        Test if instance of bucketlistApp class is successfully created
        '''
        self.assertIsInstance(
            self.current, BucketlistApp,
            msg='The object should be an instance of the BucketlistApp class')

    def test_if_user_can_sign_up(self):
        '''
        Test to check if users are added to users dictionary
        '''
        person1 = self.current.signup('Thegaijin', 'pswd', 'pswd')
        self.assertIn('Thegaijin', self.user_names,
                      msg='The user was not able to sign up')

    def test_user_confirmation_password(self):
        '''
        Test to check if user entered correct confirmation password
        when signing up
        '''
        self.current.signup('username', 'pswd', 'pswd')
        self.assertEqual(
            'pswd', 'pswd', msg="The password and confirmation password don't match")

    def test_if_user_already_exists(self):
        '''
        Test if the username enter at signup already exists in the system
        '''
        self.current.signup('username', 'pswd', 'pswd')
        self.current.signup('username', 'pswd', 'pswd')
        self.assertNotIn('username2', self.user_names,
                         msg='A user by that name already exists')

    def test_if_user_can_login(self):
        '''
        Test if the username and password combination entered at login
        exists in the users dictionary
        '''
        self.current.login('username', 'password')
        password = self.test_dict.get('username')
        self.assertEqual(password, 'password')

    def test_if_user_was_logged_out(self):
        '''
        Test if a username is removed from loggedin list on logout
        '''
        self.current.logout('username')
        self.assertNotIn('username', self.loggedin)

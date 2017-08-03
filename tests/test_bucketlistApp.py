import unittest
from app.models.bucketlistApp import BucketlistApp
from app.models.bucketlistApp import User


class BucketlistAppTestCase(unittest.TestCase):
    """Testing the functionality of the methods in
    the BucketlistApp class
    """

    def setUp(self):
        self.current = BucketlistApp()
        self.users = self.current.users
        self.new_user = User(1, 'username', 'password')

    def test_bucketlistApp_instance(self):
        """Test if instance of bucketlistApp class is
        successfully created
        """
        self.assertIsInstance(
            self.current, BucketlistApp,
            msg="The object should be an instance of the BucketlistApp class")

    def test_if_user_already_exists(self):
        """Test if the username enter at signup already exists
        in the system
        """

        self.other_user = User(2, 'username', 'pswd')
        self.current.signup(self.new_user)
        created = self.current.signup(self.other_user)
        self.assertFalse(created, msg="A user by that name already exists")

    def test_if_user_can_sign_up(self):
        """Test to check if users are added to users dictionary"""

        self.current.signup(self.new_user)
        self.assertIn(self.new_user.username, self.users,
                      msg="The user was not able to sign up")

    def test_if_user_can_login(self):
        """Test if the username and password combination entered at login
        exists in the users dictionary
        """
        self.current.signup(self.new_user)
        self.current.login("username", "password")
        self.assertEqual("password", self.users["username"].pswd_hash,
                         msg="The username and password combination does not exist")

    ''' def test_if_user_was_logged_out(self):
        """Test if a username is removed from loggedin list on logout"""
        self.current.login("Thegaijin", "pswd")
        self.current.logout("username")
        self.assertNotIn("username", self.loggedin,
                         msg="The user was not logged out") '''

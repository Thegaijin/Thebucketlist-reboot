import unittest
from app.models.users import User
from app.models.lists import Lists
from app.models.items import Items


class UserTestCase(unittest.TestCase):
    '''
    Testing the functionality of the methods in the User class
    '''

    def setUp(self):
        self.user = User('username')
        self.new_list = Lists()
        self.user_lists = self.user.bucketlists
        self.buckets = self.user.usersbuckets

    def test_creating_list(self):
        '''
        Test if lists are added to the lists dictionary
        '''
        list1 = self.user.create_list('username', 'listname1', 'details1')
        list2 = self.user.create_list('username', 'listname2', 'details2')
        self.assertIn('username', self.user_lists)
        list_count = len(self.user_lists['username'])
        self.assertEqual(list_count, 2)

    def test_if_user_list_already_exists(self):
        new_list = self.user.create_list('username', 'listname', 'details')
        self.assertNotIn('username', self.user_lists)

    def test_if_list_already_in_user_list(self):
        new_list = self.user.create_list('username', 'listname', 'details')
        # TODO: Finish the test(has to check the values of the dictionary which
        # is a list)

    def test_view_list_method(self):
        '''
        Test if list is displayed as long as it exists
        '''
        viewed = self.user.view_list('username', 'listname')
        self.assertTrue(viewed)

    def test_if_list_is_updated_on_update(self):
        '''
        Test if a list is updated
        '''
        self.user.update_list('username', 'listname', 'details')

        self.assertEqual()

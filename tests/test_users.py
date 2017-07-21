import unittest
from app.models.users import User
from app.models.lists import Lists


class UserTestCase(unittest.TestCase):
    '''
    Testing the functionality of the methods in the User class
    '''

    def setUp(self):
        self.user = User('username')
        self.user_lists = self.user.bucketlists

    def test_User_instance(self):
        '''
        Test if instance of User class is successfully created
        '''
        self.assertIsInstance(
            self.user, User,
            msg='The object should be an instance of the User class')

    def test_creating_list(self):
        '''
        Test if lists are added to the lists dictionary
        '''
        self.user.create_list('username', 'listname', 'details')
        self.assertIn('listname', self.user_lists['username'],
                      msg='The list was not created')

    def test_if_list_in_user_list(self):
        '''
        Test if a list has already been added to the users lists
        '''
        self.user.create_list('username', 'listname', 'details')
        bucketlist = self.user_lists['username']
        self.assertIn('listname', bucketlist,
                      msg='A list by that name already exists')

    def test_view_list_method(self):
        '''
        Test if list is displayed as long as it exists
        '''
        viewed = self.user.view_list('username', 'listname')
        self.assertTrue(viewed)

    def test_if_list_updated_on_update(self):
        '''
        Test if a list is updated
        '''
        self.user.create_list('username', 'listname', 'details')
        updatedlist = self.user.update_list(
            'username', 'listname', 'newdetails')

        ''' self.assertEqual(updatedlist.listname, 'listname') '''
        self.assertEqual(updatedlist.details, 'newdetails',
                         msg='The details were not updated')

    def test_list_deletion(self):
        '''
        Test if list is deleted from users lists
        '''
        newlists = self.user.delete_list('username', 'listname')
        self.assertNotIn('listname', newlists)

    def test_add_item_to_list(self):
        '''
        Test if an item is added to a list
        '''
        self.user.create_list('username', 'listname', 'details')
        added_item = self.user.add_item('username', 'listname', 'item')
        print(added_item)
        self.assertIn('item', added_item)

    def test_view_item_in_list(self):
        '''
        Test if item is displayed as long as it exists
        '''
        viewed = self.user.view_item('username', 'listname', 'item')
        self.assertTrue(viewed)

    def test_update_item_in_list(self):
        '''
        Test if an item is updated
        '''
        self.user.create_list('username', 'listname', 'details')
        added_item = self.user.add_item('username', 'listname', 'item')
        updated = self.user.update_item(
            'username', 'listname', 'item', 'newitem')
        self.assertIn('newitem', updated)

    def test_item_deletion(self):
        '''
        Test if item is deleted from users list items
        '''
        item_list = self.user.delete_item('username', 'listname', 'item')
        self.assertNotIn('item', item_list, msg='The item was not deleted')

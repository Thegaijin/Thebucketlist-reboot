import unittest
from app.models.lists import Lists


class ListTestCase(unittest.TestCase):

    def setUp(self):
        self.new_list = Lists('listname', 'password')

    def test_Lists_instance(self):
        '''
        Test if instance of List class is successfully created
        '''
        self.assertIsInstance(
            self.new_list, Lists,
            msg='The object should be an instance of the Lists class')

class User(object):
    '''
    The User clas is used to create, edit, update and delete bucketlists.
    It is also used to add, view, update, and delete items from the lists
    '''

    def __init__(self, username):
        self.username = username
        self.bucketlists = {}
        self.usersbuckets = []

    def create_list(self, username, listname, details):
        '''
        Method to create lists
        :param username:
        :param listame:
        :param details:
        '''
        pass

    def view_list(self, username, listname):
        '''
        method to view the properties of a list
        :param username:
        :param listname:
        '''
        pass

    def update_list(self, username, listname='', details=''):
        '''
        method to update the properties of a list
        :param username:
        :param listname:
        :param details:
        '''
        pass

    def delete_list(self, username, listname):
        '''
        Method to delete a list
        :param username:
        :param listname:
        '''
        pass

    def add_item(self, username, listname, item):
        '''
        method to add items to a list
        :param username:
        :param listname:
        :param item:
        '''
        pass

    def view_item(self, username, listname, item):
        '''
        method to view the properties of an item
        :param username:
        :param listname:
        :param item:
        '''
        pass

    def update_item(self, username, listname, item):
        '''
        method to update the properties of an item
        :param username:
        :param listname:
        :param item:
        '''
        pass

    def delete_item(self, username, listname, item):
        '''
        method to delete an item
        :param username:
        :param listname:
        :param item:
        '''
        pass

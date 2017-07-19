class User(object):
    '''
    The User clas is used to create, edit, update and delete bucketlists.
    It is also used to add, view, update, and delete items from the lists
    '''

    def __init__(self, username):
        self.username = username
        self.bucketlists = {}

    def create_list(self, username, listname, details):
        '''
        Method to create lists
        :param username:
        :param listame:
        :param details:
        '''
        pass

    def view_list(self):
        pass

    def update_list(self):
        pass

    def delete_list(self):
        pass

    def add_item(self):
        pass

    def view_item(self):
        pass

    def update_item(self):
        pass

    def delete_item(self):
        pass

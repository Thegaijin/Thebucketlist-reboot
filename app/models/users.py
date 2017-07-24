# /app/models/users.py

from .lists import Lists


def checker(func):
    """Decorator function that takes in a function 

    Keyword arguments:
    func -- function to be decorated
    """

    def check_list(self, *args):
        '''Function checking if username and list in users lists exist

        Keyword arguments:
        self
        *args -- arbtrary number of arguments depending on function
        '''
        if args[0] not in self.user_lists:
            return False
        return func(self, *args)
    return view_list


class User(object):
    """The User clas is used to create, edit, update and delete bucketlists.
    It is also used to add, view, update, and delete items from the lists
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_lists = {}

    def create_list(self, listname, details):
        """Method to create lists

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the bucketlist to create
        details -- What the bucketlist is about
        """

        if listname not in self.user_lists:
            new_list = Lists(listname, details)
            self.user_lists[listname] = new_list
            return listname
        return "A list by that name already exists"

    @checker
    def view_list(self, listname):
        """Method to view a list
        
        Keyword Arguments:
        listname -- The name of the list to view
        """ 
        the_list = self.user_lists[listname]
        return True

    @checker
    def update_list(self, listname, details=""):
        """method to update the properties of a list

        Keyword Arguments:
        listame -- The name of the bucketlist to update
        details -- The new property of the bucketlist
        """
        updatedlist = Lists(listname, details)
        self.user_lists[listname] = updatedlist
        return updatedlist

    @checker
    def delete_list(self, listname):
        """Method to delete a list

        Keyword Arguments:
        listame -- The name of the bucketlist to delete
        """
        del(self.user_lists[listname])
        return self.user_lists

    @checker
    def add_item(self, listname, item):
        """method to add items to a list

        Keyword Arguments:
        listame -- The name of the list to update
        item -- name of the item to add to the bucketlist
        """
        list_to_update = self.user_lists[listname]
        list_to_update.items.append(item)
        return list_to_update.items

    def view_item(self, listname, item):
        """method to view the properties of an item

        Keyword Arguments:
        listame -- The name of the list to update
        item -- name of the item in the bucketlist to view
        """
        item_list = self.user_lists[listname].items
        if item in item_list:
            return True

    @checker
    def update_item(self, listname, item, item_edit):
        """method to update the properties of an item

        Keyword Arguments:
        listame -- The name of the list to update
        item -- name of the item to edit
        item_edit -- the edit to the item
        """
        item_list = self.user_lists[listname].items
        item_index = item_list.index(item)
        item_list.remove(item)
        item_list.insert(item_index, item_edit)
        return item_list
        # FIXME: Incomplete functionality

    @checker
    def delete_item(self, listname, item):
        """method to delete an item

        Keyword Arguments:
        listame -- The name of the list to update
        item -- name of the item to delete from the bucketlist
        """
        item_list = self.user_lists[listname].items
        item_list.remove(item)
        return item_list


# CALLING THE FUNCTIONS: Testing functionality
new = User("Thegaijin", "tinktink")
print(new.create_list("Travel", "Places to go"))
print(new.add_item("Travel", "Mt Kenya"))
print(new.add_item("Travel", "Tsavo"))
print(new.add_item("Travel", "Gulu"))
print(new.update_item("Travel", "Tsavo", "Jinja"))
print(new.delete_item("Travel", "Gulu"))
print(new.view_list("Travel")) 

from .lists import Lists


def checker(func):
    """Decorator function that takes in a function 

    Keyword arguments:
    func -- function to be decorated
    """

    def view_list(self, *args):
        '''Function checking if username and list in users lists exist

        Keyword arguments:
        self
        *args -- arbtrary number of arguments depending on function
        '''
        if args[0] not in self.bucketlists:
            return "The user has no lists at the moment"

        if args[1] not in self.bucketlists.get(args[0]):
            return False
        return func(self, *args)
    return view_list


class User(object):
    """The User clas is used to create, edit, update and delete bucketlists.
    It is also used to add, view, update, and delete items from the lists
    """

    def __init__(self, username):
        self.username = username
        self.bucketlists = {}
        self.user_lists = {}

    def create_list(self, username, listname, details):
        """Method to create lists

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the bucketlist to create
        details -- What the bucketlist is about
        """

        if username not in self.bucketlists:
            self.bucketlists[username] = self.user_lists

        if listname not in self.bucketlists[username]:
            new_list = Lists(listname, details)
            self.user_lists[listname] = new_list
            return self.bucketlists
        return "A list by that name already exists"

    @checker
    def view_list(self, username, listname):
        the_lists = self.bucketlists[username]
        the_list = the_lists[listname]
        return True

    @checker
    def update_list(self, username, listname, details=""):
        """method to update the properties of a list

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the bucketlist to update
        details -- The new property of the bucketlist
        """
        the_lists = self.bucketlists[username]
        updatedlist = Lists(listname, details)
        the_lists[listname] = updatedlist
        return updatedlist

    @checker
    def delete_list(self, username, listname):
        """Method to delete a list

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the bucketlist to delete
        """
        the_lists = self.bucketlists[username]
        del(the_lists[listname])
        return the_lists

    @checker
    def add_item(self, username, listname, item):
        """method to add items to a list

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the list to update
        item -- name of the item to add to the bucketlist
        """
        the_lists = self.bucketlists[username]
        list_to_update = the_lists[listname]
        list_to_update.items.append(item)
        return list_to_update.items

    def view_item(self, username, listname, item):
        """method to view the properties of an item

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the list to update
        item -- name of the item in the bucketlist to view
        """
        the_lists = self.bucketlists[username]
        item_list = the_lists[listname].items
        if item in item_list:
            return True

    @checker
    def update_item(self, username, listname, item, item_edit):
        """method to update the properties of an item

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the list to update
        item -- name of the item to edit
        item_edit -- the edit to the item
        """
        the_lists = self.bucketlists[username]
        item_list = the_lists[listname].items
        item_index = item_list.index(item)
        item_list.remove(item)
        item_list.insert(item_index, item_edit)
        return item_list
        # FIXME: Incomplete functionality

    @checker
    def delete_item(self, username, listname, item):
        """method to delete an item

        Keyword Arguments:
        username -- The currently logged in user's name
        listame -- The name of the list to update
        item -- name of the item to delete from the bucketlist
        """
        the_lists = self.bucketlists[username]
        item_list = the_lists[listname].items
        item_list.remove(item)
        return item_list


# TODO: Testing functionality
new = User("Thegaijin")
print(new.create_list("Thegaijin", "Travel", "Places to go"))
print(new.add_item("Thegaijin", "Travel", "Mt Kenya"))
print(new.add_item("Thegaijin", "Travel", "Tsavo"))
print(new.add_item("Thegaijin", "Travel", "Gulu"))
print(new.update_item("Thegaijin", "Travel", "Tsavo", "Jinja"))
print(new.view_list("Thegaijin", "Travel"))

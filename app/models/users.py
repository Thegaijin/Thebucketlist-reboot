from .lists import Lists


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
        :param username:
        :param listame:
        :param details:
        """

        if username not in self.bucketlists:
            self.bucketlists[username] = self.user_lists

        if listname not in self.bucketlists[username]:
            new_list = Lists(listname, details)
            self.user_lists[listname] = new_list
            return self.bucketlists
        return "A list by that name already exists"

    def view_list(self, username, listname):
        """method to view the properties of a list
        :param username:
        :param listname:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                the_list = lists[listname]
                return True
            return False
        return "The user has no lists at the moment"

    def update_list(self, username, listname, details=""):
        """method to update the properties of a list
        :param username:
        :param listname:
        :param details:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                updatedlist = Lists(listname, details)
                lists[listname] = updatedlist
                return updatedlist
            return False
        return "The user has no lists at the moment"

    def delete_list(self, username, listname):
        """Method to delete a list
        :param username:
        :param listname:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                del(lists[listname])
                return lists
            return "The listname is not in the users lists"
        return "The user has no lists at the moment"

    def add_item(self, username, listname, item):
        """method to add items to a list
        :param username:
        :param listname:
        :param item:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                list_to_update = lists[listname]
                list_to_update.items.append(item)
                return list_to_update.items
            return "The listname is not in the users lists"
        return "The user has no lists at the moment"

    def view_item(self, username, listname, item):
        """method to view the properties of an item
        :param username:
        :param listname:
        :param item:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                item_list = lists[listname].items
                if item in item_list:
                    return True
            return "The listname is not in the users lists"
        return "The user has no lists at the moment"

    def update_item(self, username, listname, item, item_edit):
        """method to update the properties of an item
        :param username:
        :param listname:
        :param item:
        :param item_edit:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                item_list = lists[listname].items
                item_index = item_list.index(item)
                item_list.remove(item)
                item_list.insert(item_index, item_edit)
                return item_list
                # FIXME: Incomplete functionality
            return "The listname is not in the users lists"
        return "The user has no lists at the moment"

    def delete_item(self, username, listname, item):
        """method to delete an item
        :param username:
        :param listname:
        :param item:
        """
        if username in self.bucketlists:
            lists = self.bucketlists.get(username)
            if listname in lists:
                item_list = lists[listname].items
                item_list.remove(item)
                return item_list
            return "The listname is not in the users lists"
        return "The user has no lists at the moment"


# TODO: Testing functionality
new = User("Thegaijin")
print(new.create_list("Thegaijin", "Travel", "Places to go"))
print(new.add_item("Thegaijin", "Travel", "Mt Kenya"))
print(new.add_item("Thegaijin", "Travel", "Tsavo"))
print(new.update_item("Thegaijin", "Travel", "Tsavo", "Jinja"))

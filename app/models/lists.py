# app/models/lists.py


class Lists(object):
    """The List class is for creating List objects to hold
    the properties of a list 
    """

    def __init__(self, id, listname, details):
        self.items = []
        self.id = id
        self.listname = listname
        self.details = details

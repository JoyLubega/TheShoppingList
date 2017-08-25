from .items import Item
from .shoppinglists import SList
class User:
    def __init__(self, email, password, name=None):
        """
        Initiates class User
        :param email:
        :param password:
        :param name:
        """
        self.email = email
        self.password = password
        self.name = name
        self.slist = []
        self.id = None

    def create_list(self, list_name):
        """
        :param slist:
        """
        #Checkin if  the list_name_already exists
        if [existing_list for existing_list in self.slist
            if existing_list.name == list_name]:
            return False
        new_list = SList(list_name)
        self.slist.append(new_list)
        return True


    def update_list(self, list_name, new_list_name,
                    ):
        """
        :param list_name:
        :param new_list_name:

        """
        lst = self.get_list_from_name(list_name)
        if lst:
            lst[0].name = new_list_name

    def get_lists(self):
        """
        view all
        Returns list of all user's lists
        """
        return self.slist

    def get_single_list(self, list_name):
        """
        Gets a single list with given name
        :param list_name:
        """
        for mylist in self.slist:
            if mylist.name == list_name:
                return mylist
        # lst = self.get_list_from_name(list_name)
        # return lst[0]

    def delete_list(self, list_name):
        """
        Deletes a user's lists
        :param list_name:
        """
        # lst = self.get_list_from_name(list_name)
        # self.slist.remove(lst)
        for the_list in self.slist:
            if the_list.name == list_name:
                self.slist.remove(the_list)

    def add_item(self, list_name, item, price):
        """
        Adds an item to a list
        :param list_name:
        :param item:
        :param price:
        """
        for mylist in self.slist:
            if mylist.name == list_name:
                my_item = Item(item,price)
                mylist.items.append(my_item)
                

    def edit_item(self, list_name, item_name, new_item_name,new_price,status):

        """
        Edit (update) an item in a list
        :param list_name:
        :param item_name:
        :param new_item_name:
        :param price:
        """
        for mylist in self.slist:
            if mylist.name == list_name:
                for item in mylist.items:
                    if item.name == item_name:
                        item.name = new_item_name
                        item.price = new_price
                        item.status = status

        # lst = self.get_list_from_name(list_name)
        # item = [item for item in lst[0].items
        #         if item.name == item_name and item.price == new_price]
        # if item:
        #     item[0].name = new_item_name
        #     item[0].status = status

    def get_items(self, list_name):
        """
        view all
        Returns a list of items from a list
        :param list_name:
        :param price:

        """
        for userlist in self.slist:
            if userlist.name == list_name:
                return userlist.items
        # lst = self.get_list_from_name(list_name)
        # return lst

    def get_single_item(self, list_name, item_name):
        lst = self.get_list_from_name(list_name)
        item = [item for item in lst[0].items if item.name == item_name]
        return item[0]

    def get_list_from_name(self, list_name):
        """
        gets  a list object using a  list name only
        :param list_name:
        """
        return [lst for lst in self.slist
                if lst.name == list_name]

    def delete_item(self, list_name, item_name):
        """
        Deletes an item from a list
        :param list_name:
        :param item_name:
        """
        lst = self.get_list_from_name(list_name)
        item = [item for item in lst[0].items if item.name == item_name]
        lst[0].items.remove(item[0])
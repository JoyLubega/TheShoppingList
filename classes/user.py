class User:
    def __init__(self, email, password, name=None) -> None:
        """
        Initiates class User
        :param email:
        :param password:
        :param name:
        """
        self.email = email
        self.password = password
        self.name = name
        self.mylists = []
        self.id = None

    def create_list(self, slist):
        """RRRRRRRRR
        :param slist:
        """
        # Checkin if  the list_name_already exists
        if [existing_list for existing_list in self.mylists
            if existing_list.name == slist.name]:
            return False
        self.mylists.append(slist)
        return True


    def edit_list(self, list_name, new_list_name,
                    ) -> None:
        """
        :param list_name:
        :param new_list_name:

        """
        lst = self.get_list_from_name(list_name)
        if lst:
            lst[0].name = new_list_name

    def get_mylists(self):
        """
        view all
        Returns list of all user's lists
        """
        return self.mylists

    def get_single_list(self, list_name):
        """
        Gets a single list with given name
        :param list_name:
        """
        lst = self.get_list_from_name(list_name)
        return lst[0]

    def delete_list(self, list_name) -> None:
        """
        Deletes a user's lists
        :param list_name:
        """
        lst = self.get_list_from_name(list_name)
        self.mylists.remove(lst[0])

    def add_item(self, list_name, item, price):
        """
        Adds an item to a list
        :param list_name:
        :param item:
        :param price:
        """
        lst = self.get_list_from_name(list_name)
        item_price = self.price
        lst[0].items.append(item)

    def edit_item(self, list_name, item_name, new_item_name,price,new_price,status):

        """
        Edit (update) an item in a list
        :param list_name:
        :param item_name:
        :param new_item_name:
        :param price:
        """
        lst = self.get_list_from_name(list_name)
        item = [item for item in lst[0].items
                if item.name == item_name and item.price == new_price]
        if item:
            item[0].name = new_item_name
            item[0].status = status

    def get_items(self, list_name,price):
        """
        view all
        Returns a list of items from a list
        :param list_name:
        :param price:

        """
        lst = self.get_list_from_name(list_name)
        return [lst[0].items,lst[0].price]

    def get_single_item(self, list_name, item_name):
        lst = self.get_list_from_name(list_name)
        item = [item for item in lst[0].items if item.name == item_name]
        return item[0]

    def get_list_from_name(self, list_name):
        """
        gets  a list object using a  list name only
        :param list_name:
        """
        return [lst for lst in self.mylists
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
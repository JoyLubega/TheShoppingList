import unittest
import sys
import os

sys.path.append(os.path.abspath('../classes'))
#from calculator import simpleCalc
#from shoppinglists import SList

from classes.user import User
from classes.shoppinglists import SList
from classes.items import Item


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):

        self.user = User('jollankent@gmail.com.com', 'password', 'joy')
        self.slist = SList('joyBirthday')
        self.item = Item('cake', 2000)


    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_create_list(self):
        """Should succesfully added list"""
        self.user.create_list(self.slist)
        index = len(self.slist) - 1
        self.assertEqual(self.user.slist[index].name, 'travel')


    def test_create_list_that_already_exists(self):
        """Should return false if list name already exists"""
        self.user.create_list(self.slist)
        self.assertFalse(self.user.create_list(self.slist))

    def test_update_list(self):
        """Should test for update list"""
        self.user.create_list(self.slist)
        new_list_name = ''
        self.user.update_list(self.slist.name,new_list_name, )
        self.assertEqual(self.slist.name, new_list_name)


    def test_get_user_list(self):
        #Should check that a user can fetch all their lists
        self.slist = SList('joybirthday')
        self.user.create_list(self.slist)
        self.assertIsInstance(self.user.get_lists(), list)
        self.assertEqual(len(self.user.get_lists()), 1)

    def test_get_single_list(self):
        """Should check getting a list"""
        self.slist = SList('travel')
        self.user.create_list(self.slist)
        lst = self.user.get_single_list('travel')
        self.assertEqual(self.slist.name, 'travel')


    def test_delete_list(self):
        """Should check if list is deleted by user"""
        self.slist = SList('joybirthday')

        self.user.create_list(self.slist)

        self.assertEqual(len(self.user.get_lists()), 1)
        self.user.delete_list('joybirthday')
        self.assertEqual(len(self.user.get_lists()), 0)

    def test_user_add_item_to_list(self):
        """Should check if item is successfully added to list"""
        list_name = 'joybirthday'
        item1 = Item('cake', 3000)

        self.user.create_list(self.user.slist)
        self.user.add_item(list_name, self.item,price)
        index = len(self.slist.items) - 1
        self.assertEqual(self.slist.items[index].name, 'cake')

    def test_user_edit_item_in_list(self):
        """Should check if an item in a list is updated """
        list_name = 'joybirthday'
        item_name = 'cake'
        new_item_name = 'bag'
        price=10000
        self.user.create_list(self.slist)
        self.user.add_item(list_name,self.item ,price)
        index = len(self.slist.items) - 1
        self.assertEqual(self.slist.items[index].name, 'cake')
        self.user.edit_item(list_name, item_name, new_item_name, True)
        self.assertEqual(self.slist.items[index].name, 'shoes')

    def test_get_items_in_list(self):
        """Should check if the list items are well fetched"""

        list_name = 'travel'
        item1 = 'cake'
        item2 = 'soda'

        self.user.create_list(self.slist)
        self.user.add_item(list_name, item1,4000 )
        self.user.add_item(list_name, item2,3000)
        items = self.user.get_items(list_name)
        self.assertIsInstance(items, list)
        self.assertEqual(len(items), 2)

    def test_delete_item_from_list(self):
        """Should check if item is deleted from list"""
        list_name = 'joybirthday'
        price=2000
        self.user.create_list(self.slist)
        self.user.add_item(list_name, self.item,price)
        self.assertTrue([item for item in self.slist.items
                         if self.item.name == 'cake'])
        self.user.delete_item(list_name, self.item.name)
        self.assertFalse([item for item in self.slist.items
                          if self.item.name == 'cake'])


if __name__ == '__main__':
    unittest.main()
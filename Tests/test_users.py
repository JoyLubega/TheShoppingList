import unittest
import sys
import os

# sys.path.append(os.path.abspath('../classes'))
# #from calculator import simpleCalc
# #from shoppinglists import SList

from app.classes.user import User
from app.classes.shoppinglists import SList
from app.classes.items import Item


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):

        self.user = User('jollankent@gmail.com.com', 'password', 'joy')
        self.slist = SList('joybirthday')
        self.item = Item('cake', 2000)


    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_create_list(self):
        """Should succesfully added list"""
        self.user.create_list('travel')
        self.assertEqual(len(self.user.slist), 1)


    def test_create_list_that_already_exists(self):
        """Should return false if list name already exists"""
        self.user.create_list('travel')
        self.assertFalse(self.user.create_list('travel'))

    def test_update_list(self):
        """Should test for update list"""
        self.user.create_list(self.slist)
        new_list_name = 'joybirthday'
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
       # self.slist = SList('joybirthday')

        self.user.create_list('joybirthday')

        length_before = len(self.user.get_lists())
        self.user.delete_list('joybirthday')
        length_after = len(self.user.get_lists())
        self.assertEqual(length_before, length_after + 1)

    def test_user_add_item_to_list(self):
        """Should check if item is successfully added to list"""
        self.user.create_list("joybirthday")
        self.user.add_item('joybirthday', 'cake','3000')
        self.assertEqual(self.user.slist[-1].items[-1].name, 'cake')

    def test_user_edit_item_in_list(self):
        """Should check if an item in a list is updated """
        # list_name = 'joybirthday'
        # item_name = 'cake'
        # new_item_name = 'bag'
        # price=10000
        self.user.create_list('joybirthday')
        self.user.add_item('joybirthday','cake' ,3000)
        self.user.edit_item('joybirthday', 'cake', 'bag', 2000,True)
        self.assertEqual(self.user.slist[-1].items[-1].name, 'bag')

    def test_get_items_in_list(self):
        """Should check if the list items are well fetched"""

        list_name = 'travel'
        item1 = 'cake'
        item2 = 'soda'

        self.user.create_list('travel')
        self.user.add_item('travel', 'cake',4000 )
        self.user.add_item('travel', 'soda',3000)
        items = self.user.get_items('travel')
        self.assertIsInstance(items, list)
        self.assertEqual(len(items), 2)

    def test_delete_item_from_list(self):
        """Should check if item is deleted from list"""
        list_name = 'joybirthday'
        price=2000
        self.user.create_list('joybirthday')
        self.user.add_item('joybirthday','candle',10000)
        length_before= len(self.user.slist[-1].items)
        self.user.delete_item('joybirthday', 'candle')
        length_after= len(self.user.slist[-1].items)
        self.assertEqual(length_before - 1 , length_after)


if __name__ == '__main__':
    unittest.main()
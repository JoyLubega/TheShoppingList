import unittest

from user import User
from shoppinglists import SList
from item import Item


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):

        self.user = User('jollankent@gmail.com.com', 'password', 'joy')
        self.slist = SList('joyBirthday')
        self.item = Item('cake', )

    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_create_list(self):
        """Should succesfully create or added a bucket"""
        self.user.create_list(self.slist)
        index = len(self.user.slists) - 1
        self.assertEqual(self.user.slists[index].name, 'travel')


    def test_create_list_that_already_exists(self):
        """Should return false if bucket name already exists"""
        self.user.create_list(self.slist)
        self.assertFalse(self.user.create_list(self.slist))

    def test_update_bucket_functionality(self):
        """Should test for update list"""
        self.user.create_bucket(self.list)
        new_list_name = ''
        self.user.update_list(self.list.name,new_list_name, )
        self.assertEqual(self.list.name, new_list_name)


    """def test_get_user_buckets(self):
        Should check that a user can fetch all their buckets
        self.bucket1 = Bucket('travel', 'cities', 2)
        self.bucket2 = Bucket('food', 'test foods', 3)
        self.user.create_bucket(self.bucket)
        self.user.create_bucket(self.bucket2)
        self.assertIsInstance(self.user.get_buckets(), list)
        self.assertEqual(len(self.user.get_buckets()), 2)"""

    def test_get_single_bucket(self):
        """Should check getting a single bucket"""
        self.slist1 = sList('travel', 'cities', 2)
        self.user.create_list(self.slist)
        bucket = self.user.get_single_list('travel')
        self.assertEqual(slist.name, 'travel')
        self.assertEqual(slist.description, 'cities')

    def test_delete_bucket(self):
        """Should check if bucket is deleted by user"""
        self.slist1 = sList('joybirthday')
        self.slist2 = sList('donaschool')
        self.user.create_list(self.slist1)
        self.user.create_list(self.slit2)
        self.assertEqual(len(self.user.get_lists()), 2)
        self.user.delete_list('joybirthday')
        self.assertEqual(len(self.user.get_lists()), 1)

    def test_user_add_item_to_bucket(self):
        """Should check if item is successfully added to bucket"""
        list_name = 'joybirthday'
        self.user.create_list(self.list)
        self.user.add_item(list_name, self.item)
        index = len(self.list.items) - 1
        self.assertEqual(self.list.items[index].name, 'cake')

    def test_user_edit_item_in_bucket(self):
        """Should check if an item in a bucket is successfully edited """
        bucket_name = 'joybirthday'
        item_name = 'cake'
        new_item_name = 'shoes'
        self.user.create_list(self.slist)
        self.user.add_item(list_name, self.item)
        index = len(self.slist.items) - 1
        self.assertEqual(self.slist.items[index].name, 'cak')
        self.user.edit_item(list_name, item_name, new_item_name, True)
        self.assertEqual(self.slist.items[index].name, 'shoes')

    def test_get_items_in_bucket(self):
        """Should check if bucket items are well fetched"""

        list_name = 'travel'
        item1 = Item('cake')
        item2 = Item('soda')

        self.user.create_bucket(self.slist)
        self.user.add_item(list_name, item1)
        self.user.add_item(list_name, item2)
        items = self.user.get_items(list_name)
        self.assertIsInstance(items, list)
        self.assertEqual(len(items), 2)

    def test_delete_item_from_list(self):
        """Should check if item is deleted from bucket"""
        list_name = 'joybirthday'
        self.user.create_list(self.slist)
        self.user.add_item(list_name, self.item)
        self.assertTrue([item for item in self.slist.items
                         if self.item.name == 'cake'])
        self.user.delete_item(list_name, self.item.name)
        self.assertFalse([item for item in self.slist.items
                          if self.item.name == 'cake'])


if __name__ == '__main__':
    unittest.main()
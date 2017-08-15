import unittest


from item import Item

class itemsTestCase(unittest.TestCase):
    def setUp(self):

        self.item = Item('shoes')
        self.price= Item(2000)

    def test_activity_created(self):
        """Should test if activity has been created successfully"""
        self.assertIsInstance(self.item, Item)
        self.assertIsInstance(self.price, Item)

if __name__ == '__main__':
    unittest.main()
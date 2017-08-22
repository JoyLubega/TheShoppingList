import unittest

"""
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
"""
import sys
import os

sys.path.append(os.path.abspath('../classes'))
# from calculator import simpleCalc
from items import Item


class itemsTestCase(unittest.TestCase):
    def setUp(self):
        self.item = Item('shoes', 2000)

    def test_item_created(self):
        """Should test ifitem has been created successfully"""
        self.assertIsInstance(self.item, Item)
        # self.assertIsInstance(self.price, Item)


if __name__ == '__main__':
    unittest.main()

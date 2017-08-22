import unittest
"""from slist import sList"""
import sys
import os

sys.path.append(os.path.abspath('../classes'))
#from calculator import simpleCalc
from classes.shoppinglists import SList

class ListsTestCase(unittest.TestCase):
    def setUp(self):
        self.slist = SList('Joybithday')

    def test_slist_created(self):
        """Should test if bucket has been created successfully"""
        self.assertTrue(self.slist)


if __name__ == '__main__':
    unittest.main()
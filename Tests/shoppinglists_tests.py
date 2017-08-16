import unittest
"""from slist import sList"""


class ListsTestCase(unittest.TestCase):
    def setUp(self):
        self.slist = sList('Joybithday')

    def test_slist_created(self):
        """Should test if bucket has been created successfully"""
        self.assertTrue(self.slist)


if __name__ == '__main__':
    unittest.main()
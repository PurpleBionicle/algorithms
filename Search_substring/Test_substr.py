import unittest
from Search_substring import direct_passage


class Test_substr(unittest.TestCase):

    def test_find(self):
        self.assertEqual(0, direct_passage.substr_search('ab', 'a'))

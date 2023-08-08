import unittest
# import functions
from task import *

# Since we're using the same testcase class let's stick to our own sections.
#   --I put delimeters below to help ID where your tests should go.
# remember that our tests all have to start with the word "test" to be run
# to avoid naming conflicts, I propose using an abbreviation for each of our functions after the word test
# con_num = cn, my_datetime = md, conv_endian = ce
# the format I was thinking is the following: test_<abbreviation>_description(self):
# here's an example: test_ce_return_string(self):
# feel free to do it however you like, this is just my suggestion!


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # ********************** con_num ********************************
    def test_cn_import(self):
        """delete this test once you've started working on your code"""
        conv_num(8)
        self.assertTrue(True)
    # ********************** my_datetime ********************************

    def test_md_import(self):
        """delete this test once you've started working on your code"""
        my_datetime(8)
        self.assertTrue(True)
    # ********************** conv_endian ********************************

    def test_ce_import(self):
        """delete this test once you've started working on your code"""
        result = conv_endian(8)
        is_string = type(result) == str
        self.assertTrue(is_string)


if __name__ == '__main__':
    unittest.main()

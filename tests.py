import unittest
# import functions
import con_num
import my_datetime
import conv_endian

# Since we're using the same testcase class let's stick to our own sections, I'll put a delimeter below to help ID where your tests are
# remember that our tests all have to start with the word "test" to be run
# to avoid naming conflicts, I propose using an abbreviation for each of our functions after the word test
# con_num = cn, my_datetime = md, conv_endian = ce
# the format I was thinking is the following: test_<abbreviation>_description(self):
# here's an example: test_ce_return_string(self):
# feel free to do it however you like, this is just my suggestion!


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    ######################## con_num #################################
    ######################## my_datetime #################################
    ######################## conv_endian #################################
if __name__ == '__main__':
    unittest.main()

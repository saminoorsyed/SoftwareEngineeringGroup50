import unittest
from task import conv_num, my_datetime, conv_endian

# Since we're using the same testcase class let's stick to our own sections.
#   --I put delimeters below to help ID where your tests should go.
# remember that our tests all have to start with the word "test" to be run
# to avoid naming conflicts, I propose using an abbreviation for each of our
# functions after the word test:
# con_num = cn, my_datetime = md, conv_endian = ce
# the format I was thinking is the following:
# test_<abbreviation>_description(self):
# here's an example: test_ce_return_string(self):
# feel free to do it however you like, this is just my suggestion!


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # ************************* conv_num *****************************

    def test_cn_valid_int(self):
        self.assertEqual(conv_num('12345'), 12345)  # 12345

    def test_cn_valid_neg_float(self):
        self.assertEqual(conv_num('-123.45'), -123.45)  # -123.45

    def test_cn_valid_pos_float(self):
        self.assertEqual(conv_num('.45'), 0.45)  # 0.45

    def test_cn_valid_pos_float_2(self):
        self.assertEqual(conv_num('123.'), 123.)  # 123.

    def test_cn_valid_hexadecimal(self):
        self.assertEqual(conv_num('0xAD4'), 2772)  # 2772

    def test_cn_invalid_hexadecimal(self):
        self.assertIsNone(conv_num('0xAZ4'))  # None

    def test_cn_invalid_int(self):
        self.assertIsNone(conv_num('12345A'))  # None

    def test_cn_invalid_float(self):
        self.assertIsNone(conv_num('12.3.45'))  # None

    # ************************* my_datetime *************************

    def test_my_datetime_import(self):
        """delete test once you get started"""
        result = my_datetime(8)
        self.assertEqual(result, 8)

    # ************************* conv_endian *************************

    def test_ce_returns_string(self):
        """Test if conv_endian returns a string"""
        result = conv_endian(8)
        self.assertIsInstance(result, str)

    def test_ce_positive_big(self):
        result = conv_endian(954786, endian='big')
        expected_return = '0E 91 A2'
        self.assertEqual(result, expected_return)

    def test_ce_positive_default(self):
        result = conv_endian(954786)
        expected_return = '0E 91 A2'
        self.assertEqual(result, expected_return)

    def test_ce_negative_default(self):
        result = conv_endian(-954786)
        expected_return = '-0E 91 A2'
        self.assertEqual(result, expected_return)

    def test_ce_positive_little(self):
        result = conv_endian(954786, endian='little')
        expected_return = 'A2 91 0E'
        self.assertEqual(result, expected_return)

    def test_ce_negative_little(self):
        result = conv_endian(-954786, endian='little')
        expected_return = '-A2 91 0E'
        self.assertEqual(result, expected_return)

    def test_ce_incorrect_endian(self):
        result = conv_endian(num=-954786, endian='small')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

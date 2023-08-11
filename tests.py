import unittest
from task import conv_num, my_datetime, conv_endian
from datetime import datetime

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

    def test_md_returns_str(self):
        """Test if my_datetime returns a string"""
        result = my_datetime(8)
        self.assertIsInstance(result, str)

    def test_md_returns_format(self):
        """Test if my_datetime returns the correct format"""
        result = my_datetime(8)
        self.assertEqual(result, '01-01-1970')

    def test_md_zero(self):
        """Test if my_datetime sets zero to January 1st, 1970"""
        result = my_datetime(0)
        expected = '01-01-1970'
        self.assertEqual(result, expected)

    def test_md_before_ly(self):
        """Test if my_datetime returns correct date before any leapyears"""
        result = my_datetime(2 * 364 * 24 * 60 * 60)  # 12-31-1971
        expected = datetime.utcfromtimestamp(2 * 364 * 24 * 60 * 60)\
            .strftime('%m-%d-%Y')
        self.assertEqual(result, expected)

    def test_md_one(self):
        """Test if my_datetime returns correct date after one leapyear"""
        result = my_datetime(123456789)
        expected = '11-29-1973'
        self.assertEqual(result, expected)

    def test_md_many(self):
        """Test if my_datetime returns correct date after many leapyears.
        This will have one year divisible by 400 and one divisible by 100"""
        result = my_datetime(31 * 364 * 24 * 60 * 60)  # 11-23-2000
        expected = datetime.utcfromtimestamp(31 * 364 * 24 * 60 * 60)\
            .strftime('%m-%d-%Y')
        self.assertEqual(result, expected)

    def test_md_many_100(self):
        """Test if my_datetime returns correct date after many leapyears
        and current year is not a leap year"""
        result = my_datetime(9876543210)
        expected = '12-22-2282'
        self.assertEqual(result, expected)

    def test_md_many_400(self):
        """Test if my_datetime returns correct date after many leapyears
        and current year is a leap year"""
        result = my_datetime(201653971200)
        expected = '02-29-8360'
        self.assertEqual(result, expected)

    def test_md_max(self):
        """Test if my_datetime returns returns for year 9999"""
        result = my_datetime(2932775 * 24 * 60 * 60)  # 09-01-9999
         expected = datetime.utcfromtimestamp(2932775 * 24 * 60 * 60)\
            .strftime('%m-%d-%Y')
        self.assertEqual(result, expected)

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

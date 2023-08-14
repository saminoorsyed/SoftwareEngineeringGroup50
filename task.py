"""
The functions below complete the requirements
for CS-362's "Group Project: Part 2" assignment.

Functions:
- conv_num(num_str): Converts a string representation of an
  integer, floating-point, or hexadecimal number to base 10.
- convert_hexadecimal(hex_str): Helper function for conv_num,
  converts a hexadecimal string to base 10.
- convert_floating_point(float_str): Helper function for conv_num,
  converts a floating point string to base 10.
- convert_int(int_str): Helper function for conv_num,
  converts an integer string to base 10.
- my_datetime(num_sec): Converts an integer value representing seconds
  into a date in the format 'MM-DD-YYYY', with 0 representing '01-01-1970'.
- is_leap_year(year): Determines whether a given year is a leap year.
- helper_month_day(days_total, year): Calculates month and day of the month
  of a given year based on total days.
- conv_endian(num, endian='big'): Converts an integer to its hexadecimal
  representation with specified endianness.
"""


def conv_num(num_str):
    """
    Converts an integer, floating-point, or hexadecimal string
    into a base 10 number and returns the base 10 number
    """
    # checking for invalid input
    if num_str == "" or not isinstance(num_str, str):
        return None

    # checking if positive or negative
    if num_str[0] == '-':
        negative = True
        num_str = num_str[1:]
    else:
        negative = False

    # checking type of string + converting string to base 10
    if num_str.startswith('0x'):
        # hexadecimal number
        converted_num = convert_hexadecimal(num_str[2:])
    elif '.' in num_str:
        # floating-point number
        converted_num = convert_floating_point(num_str)
    else:
        # integer
        converted_num = convert_int(num_str)

    if negative:
        converted_num = -converted_num

    return converted_num


def convert_hexadecimal(hex_str):
    """
    Helper function for conv_num function.
    Converts a hexadecimal string to base 10 number.
    """
    hex_digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    num = 0
    for digit in hex_str:
        if digit not in hex_digits:
            return None
        num = num * 16 + hex_digits.index(digit)
    return num


def convert_floating_point(float_str):
    """
    Helper function for conv_num function.
    Converts a floating point string to base 10 number.
    """
    if float_str.count('.') != 1:
        return None
    if float_str[0] == '.':
        float_str = "0" + float_str
    integer_part, decimal_part = float_str.split('.')

    if not integer_part.isdigit() \
            or not all(digit.isdigit() for digit in decimal_part):
        return None

    num = 0
    fraction = 0
    denominator = 1

    for digit in integer_part:
        num = num * 10 + ord(digit) - ord('0')

    for digit in decimal_part:
        fraction = fraction * 10 + ord(digit) - ord('0')
        denominator *= 10

    return num + fraction / denominator


def convert_int(int_str):
    """
    Helper function for conv_num function.
    Converts an integer string to base 10 number.
    """
    digits = "0123456789"
    num = 0
    for digit in int_str:
        if digit not in digits:
            return None
        num = num * 10 + digits.index(digit)
    return num


def my_datetime(num_sec):
    """
    This function takes in an integer value and coverts it to a date
    Integer num_sec is an input in seconds
    Date is returned in the format 'MM-DD-YYYY' with
    0 representing '01-01-1970'
    """

    current_year = 1970

    # convert num_sex to days
    days = num_sec // (60 * 60 * 24)

    # subtract from days depending of if year is leap year
    # keep updating to next year
    while days >= 365:
        if is_leap_year(current_year):
            days -= 366
        else:
            days -= 365
        current_year += 1

    # convert total days to month and days left
    current_month, current_day = \
        helper_month_day(days, current_year)

    # add 0 in front of values less than 10
    if current_month < 10:
        current_month = '0' + str(current_month)
    if current_day < 10:
        current_day = '0' + str(current_day)

    return str(current_month) + '-' + str(current_day) +\
        '-' + str(current_year)


def is_leap_year(year):
    """
    Determine whether year is a leap year or not
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def helper_month_day(days_total, year):
    """
    Calculates month and day of month of year from an input of
    total days and current year
    """

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 1

    # adjust list for leap year
    if is_leap_year(year):
        days_in_month[1] = 29

    # subtract until days less than days in a month
    # update month
    for days in days_in_month:
        if days_total >= days:
            days_total -= days
            month += 1
        else:
            # have to add one to days to account for no 0 day
            return month, days_total + 1


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as num
    and converts it to a hexadecimal number.
    The endian type is determined by the flag endian.
    The function will return the converted number as a string
    """
    # return none if second arg is not big or little
    if endian not in ['little', 'big']:
        return None

    # set is_negative flag
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    hex_string = ''
    # array to convert bytes to hexadecimal
    hex_conv_arr = ['0', '1', '2', '3', '4', '5', '6',
                    '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    # convert to hexidecimal and append to hex_string
    while num > 0:
        # 256 bc 16 * 16 is total info in 1 byte (2 hex numbers)
        byte = num % 256
        # find values of most and least significant hex digits
        most_sig_digit = hex_conv_arr[byte // 16]
        least_sig_digit = hex_conv_arr[byte % 16]
        # append vals to hex string and add a space
        hex_string += most_sig_digit
        hex_string += least_sig_digit
        hex_string += ' '
        # find the next most significant byte
        num //= 256

    if endian == 'big':
        # reverse the order of bytes if big endian
        hex_string = ' '.join(hex_string.split()[::-1])

    if is_negative:
        hex_string = '-' + hex_string

    return hex_string.strip()

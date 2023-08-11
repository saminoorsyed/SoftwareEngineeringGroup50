# Below are the three functions that we'll be working on
# To get credit for our work, the functions all have to exist in the same file.
# Because of the way this assignment is set up, each pull request has to get
# approved by another group member.
# Rough Steps to getting approval:
# 1. create and checkout a branch of your own to work on
# 2. commit and push code to your own branch
# 3. when ready to merge to main,
#    run testing suit before submitting a pull request to merge
# 4. Send out a message on discord to ask a group member to
#    approve to approve your pull request.

# I'm just making this up as I go, so feel free to adjust the step above.
# Just communicate your changes if you make them so we're all on the same page

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

    if not integer_part.isdigit() or not all(digit.isdigit() for digit in decimal_part):
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
    current_month = ''
    current_day = 0

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
    return num_sec


def is_leap_year(year):
    """
    Determine whether year is a leap year or not
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def helper_month_day(days, year):
    """
    Calculates month and day of month of year from an input of
    total days and current year
    """

    # month and day if current year is a leap year
    # subtracts days in each month from the total days
    if is_leap_year(year):
        if days <= 31:
            return '01', days
        elif days <= 60:
            curr_day = days - 31
            return '02', curr_day
        elif days <= 91:
            curr_day = days - 60
            return '03', curr_day
        elif days <= 121:
            curr_day = days - 91
            return '04', curr_day
        elif days <= 152:
            curr_day = days - 121
            return '05', curr_day
        elif days <= 182:
            curr_day = days - 152
            return '06', curr_day
        elif days <= 213:
            curr_day = days - 182
            return '07', curr_day
        elif days <= 244:
            curr_day = days - 213
            return '08', curr_day
        elif days <= 274:
            curr_day = days - 244
            return '09', curr_day
        elif days <= 305:
            curr_day = days - 274
            return '10', curr_day
        elif days <= 335:
            curr_day = days - 305
            return '11', curr_day
        else:
            curr_day = days - 335
            return '12', curr_day
    else:

        # if current day is not a leap year
        if days <= 31:
            return '01', days
        elif days <= 59:
            curr_day = days - 31
            return '02', curr_day
        elif days <= 90:
            curr_day = days - 59
            return '03', curr_day
        elif days <= 120:
            curr_day = days - 90
            return '04', curr_day
        elif days <= 151:
            curr_day = days - 120
            return '05', curr_day
        elif days <= 181:
            curr_day = days - 151
            return '06', curr_day
        elif days <= 212:
            curr_day = days - 181
            return '07', curr_day
        elif days <= 243:
            curr_day = days - 212
            return '08', curr_day
        elif days <= 273:
            curr_day = days - 243
            return '09', curr_day
        elif days <= 304:
            curr_day = days - 273
            return '10', curr_day
        elif days <= 334:
            curr_day = days - 304
            return '11', curr_day
        else:
            curr_day = days - 334
            return '12', curr_day


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as num and converts it to a hexadecimal number.
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

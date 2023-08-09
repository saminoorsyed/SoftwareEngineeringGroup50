# Below are the three functions that we'll be working on
# To get credit for our work, the functions all have to exist in the same file.
# Because of the way this assignment is set up, each pull request has to get approved by another group member.
# Rough Steps to getting approval:
# 1. create and checkout a branch of your own to work on
# 2. commit and push code to your own branch
# 3. when ready to merge to main, run testing suit before submitting a pull request to merge
# 4. Send out a message on discord to ask a group member to approve to approve your pull request.

# I'm just making this up as I go, so feel free to adjust the step above.
# Just communicate your changes if you make them so we're all on the same page

def conv_num(num_str):
    """
    Converts an integer, floating-point, or hexadecimal string into a base 10 number and returns the base 10 number
    """
    # checking for invalid input 
    if num_str = "" or type(num_str) != str: 
        return None

    # checking if positive or negative 
    if num_str[0] == '-']:
        negative = True
        num_str = num_str[1:]
    else:
        negative = False

    # checking type of string + converting string to base 10
    if num_str.startswith('0x'):
        # hexadecimal number
        converted_num = convert_hexadecimal(num_str)
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

def convert_floating_point(floating_str):
    """
    Helper function for conv_num function.
    Converts a floating point string to base 10 number. 
    """
    return True

def convert_int(int_string):
    """
    Helper function for conv_num function. 
    Converts an integer string to base 10 number. 
    """
    return True


def my_datetime(num_sec):
    """function for Varun to work on """
    return num_sec


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

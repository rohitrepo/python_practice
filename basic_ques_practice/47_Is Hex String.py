import string

def is_hex_string (string):
    ishash = '0123456789abcdefABCDEF'

    for char in string:
        if char not in ishash:
            return False
    return True
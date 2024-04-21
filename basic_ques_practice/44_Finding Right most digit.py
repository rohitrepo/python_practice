#Finding right most digit of a string

import string

def find_right_most_digit (text):

    for char in reversed(text):
        if char.isdigit():
            return int(char)
    return -1
print (find_right_most_digit ('3.14 is Pi'))
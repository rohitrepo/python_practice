#python code to count uppercase letters in a string

import string

def count_uppercase_letters (text):
    count = 0
    for char in text:
        if char in string.ascii_uppercase:
            count += 1
        else:
            pass
    return count

print ( count_uppercase_letters('Rohit Yadav'))
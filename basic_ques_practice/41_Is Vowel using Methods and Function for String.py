import string

vowel = 'aeiouAEIOU'

def is_vowel(char):
    if char in vowel:
        return True
    else:
        return False
    
print (is_vowel('Z'))
    
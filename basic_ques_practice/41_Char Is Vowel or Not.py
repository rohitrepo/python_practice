import string

def is_vowel(char):
    if char.lower() == 'a' or char.lower() =='e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
        return True
    else:
        return False
    
print (is_vowel('Z'))
    
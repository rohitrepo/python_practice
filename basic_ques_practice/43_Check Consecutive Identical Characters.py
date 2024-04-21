#Check Consecutive identical charcters in string
import string

def has_consecutive_identical_characters (text):
    
    for i in range (0, len(text)-1):
        if text[i] == text [i+1]:
            return True
    return False
        
print ( has_consecutive_identical_characters ('book'))
#Anagram Checker

def is_anagram(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    
    if string1 == string2:
        return True
    return False
        
#Finding the world with longest length

import string

def find_longest_word(text):
    words  = text.split()
    longest_word = ''
    max_length = 0

    for word in words:
        
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word                
                
              

print(find_longest_word('Name aaaaaaaa Rawqqaaafdfffffffffffffaaaaa is thisssssfor'))

#a  = 'My Name is Rohit'
#b = a.split()
#print (len (b[0]) )
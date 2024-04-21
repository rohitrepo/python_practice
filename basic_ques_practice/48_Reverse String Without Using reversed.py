#reverse string without using reversed

def reverse_word(word):
    
    new_word = ''

    for char in word:
        print(char)
        new_word = char + new_word #here we are adding character at the beginning of existing word
    return new_word

print(reverse_word("Python"))
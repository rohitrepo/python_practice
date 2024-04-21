def are_both_even (i ,j):
    y = i % 2
    z = j % 2
    
    if y == 0 and z  == 0:
        return True
    else:
        return False

print (are_both_even(1, 4))
def get_number_of_digits (number):
    count = len(str(number))
    if number < 0:
        return int('-1')
    else:
        return count
    

print (get_number_of_digits(103))
print (get_number_of_digits(0))
print (get_number_of_digits(-14))
def is_prime(number):
    count = 0
    if number < 2:
        return False
    else:
        for i in range (2, number + 1):
            if number % i == 0:
                count += 1
        if count == 1:
            return True
        else:
            return False
    
print(is_prime(11))
        
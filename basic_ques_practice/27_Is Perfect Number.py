#Checking if a number is perfect number

# chck for boundary condition

def is_perfect_number (number):
    if number == 0:
        return False
    else:
        sum = 0
        #calculate divisor
        for i in range (1, number + 1):
            if number % i == 0:
                sum = sum + i
        
        if (sum - number) == number:
            return True
        else:
            return False

print (is_perfect_number (5))
#calculating sum of divisors of a number

def calculate_sum_of_divisors (number):
    sum = 0
    for i in range (1, number+1):
        if number % i == 0:
            sum = sum + i
    return sum
            
print (calculate_sum_of_divisors(4))
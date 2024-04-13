#Calculating Factorial

print ("Enter the number for which you want factorial")
n = int ( input () )
factorial = 1

for i in range (1, n + 1):
    factorial = factorial * i

print (f"Factorial of {n} is {factorial}")
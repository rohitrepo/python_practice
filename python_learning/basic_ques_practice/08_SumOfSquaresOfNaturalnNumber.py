#calculating sum of squares of Natural Number

print ("Enter the number till which you want to calculate sum:")
n = int ( input () )
sum = 0

for i in range (1, n + 1):
    sum = sum + i*i

print (f"The sum of first {n} natural numbers is {sum}")
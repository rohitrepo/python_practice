# prime number detection

print ("Enter a number:")
number = int ( input() )

i = 0
count = 0

for i in range (1, number + 1):
    if number % i == 0:
        count += 1
        i +=1

if count > 2:
    print("Number is not prime.")
else:
    print ("This is a prime number.")

#printing diamond pattern using for loop
#Hint 1 - Upper half need to be separately printed. Lower half separately.
#Hint 2 - can use step in range function to take odd numbers

#  *
# ***
#*****
# ***
#  *

print("Enter a number:")
num = int ( input () )

#Upper Half 

for i in range (1, num + 1, 2): #Increment by 2 to handle odd number only
    spaces = " " * ( (num - i ) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)

#Lower Half   

for i in range (num - 2, 0, -2): #decrease by 2 to handle odd number only
    spaces = " " * ( (num - i ) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)    

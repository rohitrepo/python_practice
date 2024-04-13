#printing * pattern
#*
#**
#***

print("Enter a number for star pattern:")
num = int ( input () )

i = 1

for i in range (1, num + 1 ):
    print ( "*" * i)               #if i = 2 then 2 stars should be printed. If i = 3 then three

    i += 1


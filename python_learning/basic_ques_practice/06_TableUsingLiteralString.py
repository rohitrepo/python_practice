#Table using formated String Literal 

print ("Enter a Number:")
num = int ( input () )

for i in range (1 , 10):
    multiple = num * i
    print ( f"{num} x {i} = {multiple}  ")
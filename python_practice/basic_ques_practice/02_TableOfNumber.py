#Print table of a number

print ("Enter a number:")
num = int ( input() )
res = 0

i = 0

for i in range (1, 11):
    res = (num * i )
    print ( num ,'x', i, '=', res)
    i += 1

print ("Thank you.")
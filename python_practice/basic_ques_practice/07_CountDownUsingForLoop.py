#Writing table of a number in reverse order

print ("Enter a number:")

num = int ( input () )

for i in range ( 10, 0, -1):
    multiple = num * i
    print(f"{num} * {i} = {multiple}")
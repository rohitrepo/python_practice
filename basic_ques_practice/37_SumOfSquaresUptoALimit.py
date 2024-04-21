#Sum of squares up to a limit

print("Enter a value till where you want sum of squares:")
number = int (input())
i = 1
square = 0

while i < (number + 1):
    square = square + i*i
    i += 1

print (f"sum of squares till {number} = {square}")
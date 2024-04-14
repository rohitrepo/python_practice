#Let us call an addition function inside a multiplication function

def addFunc (a, b):
    addition = a + b
    return addition

def multFunc (x, y):
    result = addFunc (x, y)
    multi = result * 2
    return multi

ans = multFunc (2, 9)

print (ans)
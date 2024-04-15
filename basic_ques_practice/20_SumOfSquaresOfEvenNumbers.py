#Let us pring sum of squares of first N Even Numbers

#n signifies first n even no. If n =1 then only 2 has to be considered

def sum_of_square (n): 
    square = 0
    for i in range (0, (n * 2)+2, 1): #my logic was correct but the border value was not taken so i aded  +2 in range
        if  i % 2 == 0:
            square = square + (i*i)
    return square

square = sum_of_square (2)
print (square)

#iterating over only even number so if loop not required
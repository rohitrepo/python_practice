def is_right_angled_triangle (side1, side2, side3):
    
    if (side1 == 0 or side2 == 0 or side3 == 0):
        print("Enter correct values. Side cannot be zero")
    elif (pow(side1, 2) == pow(side2, 2) + pow(side3, 2)) or (pow(side2, 2) == pow(side3, 2) + pow(side1, 2)) or (pow(side3, 2) == pow(side1, 2) + pow(side2, 2)):
        return True
    else:
        return False
    return False
        
print(is_right_angled_triangle(3, 4, 5))
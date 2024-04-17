#anglees should not be zero

def is_valid_triangle(angle1, angle2, angle3):
    sum = angle1 + angle2 + angle3
    if angle1 <= 0:
        return False
    if angle2 <= 0:
        return False
    if angle3 <= 0:
        return False
    if (sum == 180):
        return True
    else:
        return False
    
print (is_valid_triangle(100, 50, 90))
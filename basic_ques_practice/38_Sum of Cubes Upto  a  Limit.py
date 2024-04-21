#Limit is on sum of cubes and not on number whose sum of cubes need to be calculated

def sum_of_cubes_upto_limit (limit):
    sum = 0
    i = 1

    if limit <= 0:
        return 0
    else:
        while sum <= limit:
            sum = sum + pow(i, 3)
            i += 1
            if pow(i, 3) > limit:
                return sum
            else:
                continue    
        
print (sum_of_cubes_upto_limit (30))
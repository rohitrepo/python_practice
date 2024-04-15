#Check if age >=18 then can access library

def can_access_library(age):
    if age >= 18:
        flag = True
        print(flag)
    else:
        flag = False
        print(flag)
    return flag

can_access_library(19)
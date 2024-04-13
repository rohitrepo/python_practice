print ("Enter length of side of square:")
side = int ( input () )



for i in range (1, side + 1):
    if i == 1:
        pass
    else:
        print ()

    for j in range (1, side + 1):
        print ("*", end = "")
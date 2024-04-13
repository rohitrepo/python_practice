#Printing hollow square pattern

print ("Enter the length of side of square:")
side = int ( input () )

i = 0

for i in range (1, side + 1):
    if i == 1 or i == side:
        print ("* "*side)
    elif i > 1 and i < side:
        print ("*", "  "*(side-2), "*" )
     

           

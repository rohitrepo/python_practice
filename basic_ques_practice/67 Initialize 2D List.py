list = []

#for 3 rows and 4 columns 
# a = [  [ 1, 2, 3, 4  ]
#        [ 5, 6, 7, 8  ]      
#        [ 9, 2, 2, 1  ]
#                        ]


for i in range (0, 2):
    row = []                        #first values are appended in row
    for j in range (0, 3):
        row.append(i * 10+j)        # secondly row is added as a list to the main list
    list.append(row)



print (list)

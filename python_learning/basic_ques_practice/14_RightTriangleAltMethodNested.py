#Right triangle with Nested For Loop

print ("Enter the height of the right triangle:")
h = int ( input() )

for i in range (h):
    for j in range (i + 1):
        print ("*" * j, end = "")
    print ()
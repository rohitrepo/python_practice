
class Square:
    def __init__(self, side):
        self.side = side
        print('Side =', self.side)

    def calculate_area(self):
        if self.side <= 0:
            return -1
        else:
            return (self.side)*(self.side)


    def calculate_perimeter(self):
        if self.side <= 0:
            return -1
        else:
            return 4 *(self.side)

fig1 = Square(20)

print (fig1.calculate_area())
print (fig1.calculate_perimeter())
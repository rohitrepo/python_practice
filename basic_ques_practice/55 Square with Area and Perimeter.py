
class Square:
    def __init__(self, side):
        self.side = side
        print('Side =', self.side)

    def calculate_area(self):
        if self.side <= 0:
            return -1
        else:
            self.area = (self.side) * (self.side)
            print('Area =', self.area)

    def calculate_perimeter(self):
        if self.side <= 0:
            return -1
        else:
            self.perimeter = 4 * (self.side)
            print('Perimeter =', self.perimeter)

fig1 = Square(20)

fig1.calculate_area()
fig1.calculate_perimeter()
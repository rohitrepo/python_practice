import math

class Point:

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self, dx, dy):
        #after caling this method, the coordinates have to be (current x + dx, current y + dy)
        self.dx = dx
        self.dy = dy

        self.x = self.x + dx
        self.y = self.y + dy
        print("New Cooridates are:", self.x, ',', self.y) 

    def distance_to(self, other):
        #The Euclidean distance d between two points (x1, y1) and (x2, y2) is calculated as: 
        #d = sqrt((x2-x1)^2 + (y2-y1)^2).

        dx = self.x - other.x
        dy = self.y - other.y

        distance = math.sqrt(dx * dx + dy * dy)
        print(distance)

coordinate1 = Point(10, 20)


coordinate1.move(2, 2)
coordinate1.distance_to(coordinate1)
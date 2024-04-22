class Planet:

    def __init__(self, name):
        self.name = name

    def revolve(self):
        print("Planet revolves")
    
    def rotate(self):
        print ("Planet rotates")

    def rotate_and_revolve(self):
        self.revolve()
        self.rotate()

planet1 = Planet('Earth')
planet2 = Planet('Mars')

planet1.rotate_and_revolve()


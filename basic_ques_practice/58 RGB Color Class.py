class RGBColor:
    def __init__(self, red, green, blue):
        self.red =  red
        self.green = green
        self.blue = blue

        if (self.red <= 0 or self.red > 255 or self.green <= 0 or self.green > 255 or self.blue <= 0 or self.blue > 255):
            print("invalid color code")
        else:
            print ("Red:", self.red, "Green:", self.green, "Blue:", self.blue)


    def invert(self):
        self.red = 255 - self.red
        self.green = 255 - self.green
        self.blue = 255 - self.blue
        print ("Inverted - Red:", self.red, "Green:", self.green, "Blue:", self.blue)

color1 = RGBColor(255,0,0)

color1.invert()
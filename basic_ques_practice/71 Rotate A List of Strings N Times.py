#This code is not correct. Need to work later to modify it.

class RotateString:
    def __init__ (self, string, n):
        self.string = string
        self.n = n

    def rotate_string(self):

        self.rotated_string = ''

        for i in range (self.n):
            if i == 0:
                for char in (self.string):
                    self.rotated_string = char + self.rotated_string
            else:
                for char in (self.rotated_string):
                    self.rotated_string = char + self.rotated_string
        return self.rotated_string

string1 = RotateString('RohitYadav', 3)

print ( string1.rotate_string() )
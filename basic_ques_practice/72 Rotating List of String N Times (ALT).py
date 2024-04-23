class RotateString:
    def __init__ (self, string_list, n):
        self.string_list = string_list
        self.n = n

    def rotate_string (self):
        self.rotated_string = []

        for i in range (1):
            for j in range (len(self.string_list)-1):
                self.rotated_string[j] = self.string_list[ (len(self.string_list)-1 - j) ]

        return self.rotated_string

string1 = RotateString(['Hello', 'How', 'Are', 'You'], 2)

print ( string1.rotate_string() )
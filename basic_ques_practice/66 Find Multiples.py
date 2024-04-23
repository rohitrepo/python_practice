class FindMultiples:
    def __init__ (self, number, upper):
        self.number = number
        self.upper = upper
    
    def find_multiples (self):
        self.multiples = []
        
        for i in range (1, self.upper):
            self.multiple_value = self.number * i
            if self.multiple_value <= self.upper:
                self.multiples.append(self.multiple_value)
        
        return self.multiples


number1 = FindMultiples(25, 150)

print (number1.find_multiples())
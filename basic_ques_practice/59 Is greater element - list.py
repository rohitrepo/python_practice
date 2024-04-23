class GreaterNumber:
    def __init__ (self, number, value):
        self.number = number
        self.value = value
    
    def has_greater_element(self):

        self.largest_number = 0

        if self.number == []:
            return False
        else:
            for i in range (0, len (self.number)):
                if self.number[i] > self.value:
                    self.largest_number = self.number[i]
                else:
                    self.largest_number = self.value
            return self.largest_number


                

list1 = GreaterNumber([] , 10)

print(list1.has_greater_element())



class FactorsList:
    def __init__ (self, number):
        self.number = number

    def find_factors(self):
        self.factor = []

        if self.number <= 0:
            return "Number is negative or zero"
        else:
            for i in range (1, self.number+1): #important to note that we took self.number + 1 
                if self.number % i == 0:
                    self.factor += [i] 
                else:
                    continue
            return self.factor
        
number1 = FactorsList(12)

print(number1.find_factors())

# take care of the border cases in the for loop range
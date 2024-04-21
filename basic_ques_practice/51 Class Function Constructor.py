class MotorBike:
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name
        print("MotorBike instance created") #this will be printed every time an instance is created.
       
        

re = MotorBike(50, 'Hunter')
#re.name = 'Hunter'

print(re.speed)
print(re.name)

hero = MotorBike(10, 'Splendor')
#hero.name = 'Splendor'

print(hero.speed)
print(hero.name)
#INheritance and multiple inheritance


class Car:
    'THis is car class'

    def __init__(self, color):
        self.carColor = color
        print ("Called Car class method")

    def __str__(self): # this overloding method of base class
        return "you called {} class".format(self.__class__.__name__)
    def displayCarColor(self):
        return "Color of the {} is {}".format(self.__class__.__name__, self.carColor)

    def displayCarDetails(self):
        return "Car details are : {}".format(self.carColor)

class Swift(Car):
    'This is swift class and subclass of car class'

    def __init__(self, model, turbo, color):
        Car.__init__(self, color)
        self.swiftModel = model
        self.swiftTurbo = turbo
        print ("Called Swift class method")

    def displayCarDetails(self): #overridding your parent class method with this method
        return "{}\nSwift Car model is {} with {} turbo engine".format(self.displayCarColor(), self.swiftModel, self.swiftTurbo)

class unknowType:
    'me for simple'

    def __init__(self, owner):
        self.typeOwner = owner
        print ("Calles unknowType class")

    def displayType(self):
        return "owner name is {}".format(self.typeOwner)
    
class carModel(unknowType, Swift, Car):
    'This another CarModel sub class'

    def __init__(self, price, model, turbo, color, owner):
        super().__init__(owner)
        Swift.__init__(self, model, turbo, color)
        self.carPrice = price
        print ("Called CarModel class method")

    def carModelPrice(self):
        return "Car price is : {}".format(self.carPrice)

    def carDetails(self):
        print (self.displayCarDetails())




car1 = Swift('Dzire', '3500cc', 'Green')

print (car1)



#car1.displayCarColor()
#car1.displayCarDetails()
#print (Swift.__dict__)
print (carModel.__mro__)

car3 = carModel('Hemanth', '5lack', 'Thunder', '4500cc', 'Blue')
print (car3.displayCarColor(), end = "\n*********\n")
print (car3.displayCarDetails(), end = "\n#########\n")
print (car3.carModelPrice(), end = "\n$$$$$$$$$$$\n")
setattr(car3, 'carPrice', '6lack')
print (car3.carModelPrice(), end = "\n$$$$$$$$$$$\n")
#print (carModel.__dict__)



car2 = Car('Red')
print (car2.displayCarColor())

print (issubclass(carModel, Car))
print (issubclass(carModel, Swift))
print (issubclass(Swift, Car))
print (issubclass(Swift, carModel))

print (end = "++++++++++++++++\n")

print (isinstance(car3, carModel))
print (isinstance(car2, Car))
print (isinstance(car1, Swift))
print (isinstance(car1, Car))
print (isinstance(car3, Swift)) # car3 is instance of all it's super classes.

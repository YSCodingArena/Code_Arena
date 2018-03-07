#Overloading the operators


class student:
    'class of student'

    def __init__(self, name, age):
        self.stdName = name
        self.stdAge = age
        print ("Called {} constructor method".format(student.__name__))

    def __add__(self, other):
        return (self.stdName + other.stdName, self.stdAge + other.stdAge)

    def __sub__(self, other):
        return (self.stdName + other.stdName, self.stdAge - other.stdAge)

std1 = student('Hemanth', 26)
std2 = student('Kumar Y S', 25)
print (std1 + std2)
print (std1 - std2)

#Data hiding


class student:
    'class of student'
    
    def __init__(self, name, age, sex):
        self.stdName = name
        self.__stdAge = age #age is hidden and only available to with in class.
        self.stdSex = sex
        print ("Called {} constructor method".format(student.__name__))

    def displayName(self):
        return 'Student - Name : {}'.format(self.stdName)

    def displaySex(self):
        return 'Student - Sex : {}'.format(self.stdSex)

    def displayAge(self):
        if self.stdSex.upper() != "FEMALE":
            return "Student - Age : {}".format(self.__stdAge)
        else:
            return "You shouldn't ask girls age!."

    def __repr__(self):
        return " --> You should call with '()' to get value of object"

std1 = student('Hemanth', 26, 'male')
std2 = student('Prathibha', 25, 'female')
print (std1.displayName())
print (std1.displaySex())
print (std1.displayAge())

print (std2.displayName())
print (std2.displaySex())
print (std2.displayAge())

print (std2.__dict__)
print (std2.__module__)
print (std2.__sizeof__)
#print (std2.__stdAge) --> thorws an error
print (std2._student__stdAge) # this should work fine

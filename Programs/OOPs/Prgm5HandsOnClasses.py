#Handon - instances, instace variables and class variables

class student:
	'This is the songs class'
	count = 0
	def __init__(self, name, sex):
		self.stdName = name
		self.stdSex = sex
		student.count+=1
		print ("Totally {} students are available".format(student.count))

	def displayDetails(self):
		print ("Student datails:\n Name: {}\nSex: {}".format(self.stdName, self.stdSex))

std1 = student('Hemanth Kumar Y S', 'Male')
print (std1.__dir__())
#O/P --> ['stdName', 'stdSex', '__module__', '__doc__', 'count', '__init__', 'displayDetails', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
print (std1.__class__('Me', '23'))
#This is gonna call the class, so count incremented
#O/P -->Totally 2 students are available
#       <__main__.student object at 0x7fd64eff87b8>
print (std1.__dict__)
#O/P --> {'stdName': 'Hemanth Kumar Y S', 'stdSex': '26'}
print (std1.__module__)
#O/P --> __main__
print (std1.__doc__)
#O/P --> This is the songs class
print (getattr(std1, 'stdName')) # O/P = Hemanth Kumar Y S

#print (getattr(std1, 'stdAge')) --> thorws an error since attribute is not available

print (hasattr(std1, 'stdSex')) # O/P = True
print (hasattr(std1, 'stdAge')) # O/P = False

setattr(std1, 'stdName', "Young Star") # set stdName to 'Young Star'
print (std1.stdName)
setattr(std1, 'stdAge', 26) # if given attribute is not available, it creates new one.
print (std1.stdAge)

print (std1.__dict__) # O/P = {'stdName': 'Young Star', 'stdSex': 'Male', 'stdAge': 26}

delattr(std1, 'stdAge')
print (hasattr(std1, 'stdAge')) #op = False


print ("student.__doc__:", student.__doc__)
#O/P = student.__doc__: This is the songs class
print ("student.__name__:", student.__name__)
#O/P = student.__name__: student
print ("student.__module__:", student.__module__)
#O/P = student.__module__: __main__
print ("student.__bases__:", student.__bases__)
#O/P = student.__bases__: (<class 'object'>,)
print ("student.__dict__:", student.__dict__ )
#O/P = student.__dict__: {'__module__': '__main__', '__doc__': 'This is the songs class', 'count': 2, '__init__': <function student.__init__ at 0x7f561736e0d0>, 'displayDetails': <function student.displayDetails at 0x7f561736e158>, '__dict__': <attribute '__dict__' of 'student' objects>, '__weakref__': <attribute '__weakref__' of 'student' objects>}

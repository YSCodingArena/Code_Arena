#Overriding Methods and overloading methods

class drink:
	'This is the drink class'
	def __init__(self, dType):
		self.dType = dType
		self.dMenu = {'Green Tea':15, 'Normal Tea':10, 'Ginger Tea':15, 'Coffee':10, 'Cold Coffee':15, 'Milk':10, 'Badam Milk':15}
		print ("Order is taken, pls wait for 10 min")

	def displayPrice(self):#This method is overriden by food method.
		return "{} price is {}".format(self.dType, self.dMenu[self.dType])

class food(drink): 
	'This the food class inheriting the drink class'
	
	def __init__(self, dOrder, fOrder):
		drink.__init__(self, dOrder) #letting parent class handle the 'dOrder'and it's attributes
		self.fOrder = fOrder
		self.fMenu = {'Masala Dosa': 35, 'Normal Dosa':20, 'Onion Dosa':45, 'Idli':20, 'Idli Wada':35, 'Wada':15, 'Poori Sagu':45}

	def displayPrice(self):
		return "Drink Order : {} price is {}\nFood Order : {} price is {}".format(self.dType, self.dMenu[self.dType], self.fOrder, self.fMenu[self.fOrder])
		
	#Below 2 methods are examples of method overloading, means we are loaing our own message instead of system default message	
	def __str__(self):
	    return "--> This is the overloading method '__str__' of class {}".format(self.__class__.__name__)
	    
	def __repr__(self):
	    return "--> This is another oveloading method '__repr__' of class {}".format(self.__class__.__name__)

order1 = food('Green Tea', 'Onion Dosa')
print (order1.displayPrice())
print (order1.__dict__)
print (order1)
#This is the O/P when we run above line --> "<__main__.food object at 0x7f59d012c860>""
#But after using __str__ method return string will be displayed in place of above object value.
# O/P --> "--> This is the overloading method '__str__' of class food"

print (order1.displayPrice)
#This is the O/P when we run above line --> "<bound method food.displayPrice of <__main__.food object at 0x7f9b39a6f860>>""
#But after using __repr__ method return string will be displayed in place of above object value.
# O/P --> "<bound method food.displayPrice of --> This is another oveloading method '__repr__' of class food>""


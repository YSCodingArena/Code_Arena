#Constructor and destructor

class drink:
	'This is the drink class'
	def __init__(self, dType):
		self.dType = dType
		self.menu = {'Green Tea': 15, 'Normal Tea':10, 'Ginger Tea':15, 'Coffee':10, 'Cold Coffee':15, 'Milk':10, 'Badam Milk':15}
		#When we create the class instances, this init method will be called automatically.
		print ("Order is taken, pls wait for 10 min")

	def displayPrice(self):
		return "{} price is {}".format(self.dType, self.menu[self.dType])

	def __del__(self):
		print ("Order served to customer")

order1 = drink('Ginger Tea')
#del(order1) --> if we call this function automaticaly destructor method will be called since all the instance of the classes are destroyed.
print (order1.displayPrice())
#if we didn't call 'del()' function explicitly, '__del__' method will be called after all lines are executed.
		
		
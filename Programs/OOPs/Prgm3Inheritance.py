#inheritance

class drink:
	'This is the drink class'
	def __init__(self, dType):
		self.dType = dType
		self.dMenu = {'Green Tea':15, 'Normal Tea':10, 'Ginger Tea':15, 'Coffee':10, 'Cold Coffee':15, 'Milk':10, 'Badam Milk':15}
		#When we create the class instances, this init method will be called automatically.
		print ("Order is taken, pls wait for 10 min")

	def displayPrice(self):
		return "{} price is {}".format(self.dType, self.dMenu[self.dType])

class food(drink): 
	'This the food class inheriting the drink class'
	
	def __init__(self, dOrder, fOrder):
		drink.__init__(self, dOrder) #letting parent class handle the 'dOrder'and it's attributes
		self.fOrder = fOrder
		self.fMenu = {'Masala Dosa': 35, 'Normal Dosa':20, 'Onion Dosa':45, 'Idli':20, 'Idli Wada':35, 'Wada':15, 'Poori Sagu':45}

	def displayAmount(self):
		return "Drink Order : {}\nFood Order : {} price is {}".format(self.displayPrice(), self.fOrder, self.fMenu[self.fOrder])

order1 = food('Green Tea', 'Onion Dosa')
print (order1.displayAmount())
print (order1.displayPrice()) #Can be called the parent methods
order1.dType = 'Normal Tea' #Can be changed parent attribute
print (order1.displayAmount())
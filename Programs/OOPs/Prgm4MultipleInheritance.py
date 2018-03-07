#multiple inheritance

class drink:
	'This is the drink class'
	def __init__(self, dType):
		self.dType = dType
		self.dMenu = {'Green Tea':15, 'Normal Tea':10, 'Ginger Tea':15, 'Coffee':10, 'Cold Coffee':15, 'Milk':10, 'Badam Milk':15}
		#When we create the class instances, this init method will be called automatically.
		print ("Order is taken at {}, pls wait for 10 min".format(self.__class__.__name__))

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

class canteen(food, drink):
	'This canteen class inheriting food and drink class'
	def __init__(self, name, dOrder, fOrder):
		super().__init__(dOrder, fOrder) # when we use super() it class first parent class, which is food and no need to pass self.
		self.name = name

	def displayMenu(self):
		print ("**** Drink Menu ****")
		for item, price in self.dMenu.items():
			print (item, price)

		print ("**** Food Menu ****")
		for item, price in self.fMenu.items():
			print (item, price)

order1 = canteen("Mama's Kitchen", 'Green Tea', 'Onion Dosa')

order1.displayMenu()
print ("===============================")
print (order1.displayAmount())

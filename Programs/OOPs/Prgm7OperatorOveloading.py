#Operator Overloading

class drink:
	'This is the drink class'
	def __init__(self, dType):
		self.dOrder = dType
		self.dMenu = {'Green Tea':15, 'Normal Tea':10, 'Ginger Tea':15, 'Coffee':10, 'Cold Coffee':15, 'Milk':10, 'Badam Milk':15}
		print ("Order is taken at {}, pls wait for 10 min".format(self.__class__.__name__))

	def displayPrice(self):
		return "{} price is {}".format(self.dOrder, self.dMenu[self.dOrder])

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
		super().__init__(dOrder, fOrder)
		self.name = name

	def displayMenu(self):
		print ("**** Drink Menu ****")
		for item, price in self.dMenu.items():
			print (item, price)

		print ("**** Food Menu ****")
		for item, price in self.fMenu.items():
			print (item, price)
	
	def finalBill(self):
		return self.fMenu[self.fOrder]+self.dMenu[self.dOrder]
		
	def __add__(self, other): #'self' is first argument and 'other' is second argument that we will pass to add method.
	    return self.finalBill()+other.finalBill()

order1 = canteen("Mama's Kitchen", 'Green Tea', 'Onion Dosa')
order2 = canteen("Dosa Corner", 'Ginger Tea', 'Masala Dosa')

order1.displayMenu()
print ("===============================")
print (order1.displayAmount())
print (order2.displayAmount())
print ("===============================")
print (order1.finalBill())
print (order2.finalBill())

print (order1 + order2)
#This is error we get when we try above line since it can't add instances
#   Traceback (most recent call last):
#   File "main.py", line 53, in <module>
#     print (order1 + order2)
#TypeError: unsupported operand type(s) for +: 'canteen' and 'canteen'

# but if we add our own 'add(+)' operator above code might work.. lets see.

#After adding '__add__' method above code works fine. This is operator overloading.

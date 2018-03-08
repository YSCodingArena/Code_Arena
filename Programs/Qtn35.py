class Queue:
	mobList = []
	def __init__(self, mobile, price):
		self.mobile = mobile
		self.price = price
		Queue.mobList.append('Hi')
		
	def totalMobiles(self):
		print (Queue.mobList)
		print (hex(id(self)))
		
mob1 = Queue('Redmi 5A', 10000)
mob1.totalMobiles()
#print (mob1.__dir__())
print (__builtins__.__dir__())

#print (mob1.__class__.__dict__)
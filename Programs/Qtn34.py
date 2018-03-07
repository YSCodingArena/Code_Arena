class operatorNum:

	'This class is the sample  class to check somthing'
	def __init__(self):
		self.name = ''
		
	def displayAttributes(self):
		print ("This is the complete dict of current instance : {}".format(self.__dict__))
		
run = operatorNum()
run.displayAttributes()
run.name = 'Hemanth Kumar Y S'
run.age = 26
run.displayAttributes()
<<<<<<< HEAD
run.salary = 75000
=======
run.sez = 'Male'
>>>>>>> d52c2a5bacb7c64598a55ba9210d410ddcdefb32
run.displayAttributes()

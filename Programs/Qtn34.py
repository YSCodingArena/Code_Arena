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
run.salary = 75000
run.sex = 'Male'
run.displayAttributes()

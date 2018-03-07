#sample class declaration

class laptop:
	'This is the laptop class'
	def __init__(self):
		print ("Constructor method of class {} executed".format(self.__class__.__name__))

	def powerOptions(self, power):
		options = ["shutdown", "restart", "reboot", "signoff", "sleep"]
		if power.lower().replace(" ","") in options:
			print ("Laptop's {} operation completed".format(power))

action = laptop()
action.powerOptions('Sign Off')
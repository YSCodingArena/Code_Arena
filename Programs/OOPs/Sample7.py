def outerFunc(function):
	print ("Printing before calling constructor!!")
	def innerFun(*args):
		print ("I'm printing aftercalling the function!!")
		print (type(*args))
		return function(*args)
	return innerFun
	
@outerFunc
def add(x,y):
	return x+y
	
print (add(1,2))
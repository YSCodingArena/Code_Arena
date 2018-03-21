class simple:
  def __init__(self):
    print ("Simple constructor called")
  def whoami(self, x, y):
    print ("I'm simple Static Method!??")
    print ("Passed argument : {} and {}".format(x,y))
    
  @staticmethod
  def secondTime():
    print ("Is i'm normal method!??")
    
class second(simple):
  
  def __init__(self):
    super().__init__()
    print ("second Constructor called")
  def whoami(self):
    super(second, self).whoami(20,40)
    print ("I'm second Static Method!??")
    
  def display(self):
    print ("Printing stuff")
ob1 = second()
ob1.whoami()
#second.whoami(ob1)
ob1.secondTime()
print (simple.__dict__)
print (second.__dict__)
print (ob1.__dir__())
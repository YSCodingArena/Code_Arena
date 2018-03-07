class __SimpleError(Exception):
  pass

try:
  raise __SimpleError('Not found')
except __SimpleError as error:
  print (error)
except Exception as error:
  print ("Error :",error)


class sample:
  
  def runMe(self):
    print ("It's runMe() method!!, and this class called this method: ", self.__class__.__name__)

  def whatsup(self):
    raise NotImplementedError("You're calling not implemented methods!!")
    
class simple(sample)  :
  def name(self):
    print ("Class Name :",self.__class__.__name__)
    
  def whatsup(self):
    print ("MRO :", self.__class__.__mro__)
    print ("What's Up!!")
    
try:
  hi = simple()
  so = sample()
  so.runMe()
  #so.whatsup()
  hi.runMe()
  hi.name()
  #print (simple.__mro__)
  hi.whatsup()
  
except NotImplementedError as error:
  print (error)
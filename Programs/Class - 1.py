#===============================================================================
# class Student:
#     ''' Data of student'''
#     def __init__(self, first, last, score):
#         self.first = first
#         self.last = last
#         self.score = score
#         self.email = first.lower() + "." + "".join(last.split(" ")).lower() + "@gmail.com"
#         
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#         
# 
# std_1 = Student('Hemanth', 'Kumar Y S', 510)
# #std_2 = Student()
# 
# #std_1.first = "Hemanth"
# #std_1.last = "Kumar Y S"
# #std_1.email = "hemanth.kumarys@gmail.com"
# 
# #print (std_1.first, std_1.last)
# #print (std_1.__dict__)
# print ('score = {}, email = {}'.format(std_1.score, std_1.email))
# print (std_1.fullname())
# print (Student.fullname(std_1))
#===============================================================================



class calculation:
    var1 = 1
    
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def increVar(self):
        calculation.var1 += 5        
        
    def addNum(self):
        self.increVar()
        print (self.a + self.b)
    
    def subNum(self):
        self.increVar()
        print (calculation.var1 - self.a)
    

calc = calculation(10,20)
calc1 = calculation(30,40)
calc.addNum()
calc1.subNum()

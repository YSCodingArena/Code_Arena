'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''


##class numIterator:
##
##    def __init__(self, n):
##        self.num = n
##
##    def generator(self):
##        return [x for x in range(self.num) if x % 7 == 0]
##
##numGen = numIterator(20)
##print (numGen.generator())

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j # needs to learn about yields

for i in putNumbers(100):
    print (i)

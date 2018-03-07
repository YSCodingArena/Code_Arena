'''
Define a class named American which has a static method called printNationality.
'''


class america:

    @staticmethod
    def printNationality():
        print ("I'm an american")

nation = america()
nation.printNationality()
america.printNationality()


print (america.__dict__)

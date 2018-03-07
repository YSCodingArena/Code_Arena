'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class simpleTest:

    def getString(self):
        self.pString = input("Enter string : ")

    def printString(self):
        print ("Inputed string is ,", self.pString.upper())

f = simpleTest()
f.getString()
f.printString()

#another way of telling

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()

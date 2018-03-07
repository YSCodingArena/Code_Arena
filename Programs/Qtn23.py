'''
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
'''

print (sorted.__doc__, end = "\n**************************************")
print (pow.__doc__, end = "\n**************************************")

def  square(x):
    '''
    It takes one argument and it returns the square of given integer.

    Variable type should be numeric

    Code: return x**2
    '''
    try:
        return x**2
    except Exception as error:
        return error

val = '2'
print (square(int(val)))
print (square(val))

print (pow(2,2))

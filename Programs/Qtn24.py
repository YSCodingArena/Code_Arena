def displayDict():
    samDict = {}
    for val in range(1, 21):
        samDict[val] = val**2

    return samDict

print (list(displayDict().values()))

a = map(str, [1,2,3,4,5,6,7,8,9,10])
print (list(a))

a = [1,2,3]; b = ['one', 'two', 'three', 'four']#; c = ['I', 'II', 'III']
print (list(zip(a,b)))

'''
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (list(evenNumbers))

print (staticmethod.__doc__)
print (classmethod.__doc__)

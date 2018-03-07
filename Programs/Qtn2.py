'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

#solution 1:
num = input("Enter a number to calculate fatorials: ")
val = 1
for n in range(1, int(num)+1):
    val*=n

print (val)

#solution 2:

def fact(x):
    if x == 0:
        return 1

    return x*fact(x-1)

print (fact(int(num)))


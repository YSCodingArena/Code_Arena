'''
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

'''

print (",".join([str(x) for x in range(11) if x % 2 == 0]))


'''
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70
'''

def printNum(n):
    for val in range(1,n+1):
        if val % 5 == 0 and val % 7 == 0:
            yield val


num = input()
result = printNum(int(num))
for i in result:
    print (i)

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''
#solution 1

def binToDec(num):
    decList = [8, 4, 2, 1]
    val = 0
    for i,j in enumerate(num):
        if j == '1':
            val+=decList[i]
    if val % 5 == 0:
        return True
    return False

strList = input().rstrip().split(",")
for strs in strList:
    if binToDec(strs):
        print(strs, end = ", ")


#Solution 2

strList = input().rstrip().split(",")
for strs in strList:
    if int(strs, 2) % 5 == 0: # int can be used for convert decimals.
        print(strs, end = ",")

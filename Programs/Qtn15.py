'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

num = input()
num2 = num+num
num3 = num2 + num
num4 = num3 + num

print (int(num)+int(num2)+int(num3)+int(num4))

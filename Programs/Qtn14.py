'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

strip = input()
lower = upper = 0
for let in strip:
    if let.islower():
        lower+=1
    if let.isupper():
        upper+=1

print ("UPPER CASE", upper)
print ("LOWER CASE", lower)

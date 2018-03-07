'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

sentance = input().rstrip()
print (sentance)
LETTERS = DIGITS = 0
for letter in sentance:
    if letter.isdigit():
        DIGITS+=1
    if letter.isalpha():
        LETTERS+=1
print ("DIGITS", DIGITS)
print ("LETTERS", LETTERS)
    

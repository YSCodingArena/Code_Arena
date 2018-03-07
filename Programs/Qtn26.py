'''
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import re

email = input()

p1 = re.compile(r'(\w+)@')
result1 = p1.match(email) # used match here since 'match' will only work which, when string start with given pattern.

print (result1.group(1))


'''
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

p2 = re.compile(r'@(\w+)')
result2 = p2.search(email)#'search' method will search whole string for pattern

print (result2.group(1))

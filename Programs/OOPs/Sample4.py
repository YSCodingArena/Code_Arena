import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


#print (dir(re))

#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # use () to group the letters.

#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.[a-z]+')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#result = pattern.finditer(urls)
#for i in result:
#    print (i.group(2)) # will retuen the groups.

subed_urls = pattern.sub(r'\2\3', urls)
print (subed_urls)




#print (re.match('[a-z]', 'temp'))

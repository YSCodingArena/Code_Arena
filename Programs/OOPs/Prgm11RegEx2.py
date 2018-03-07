import os
import re

os.chdir(r"E:\\Hemanth\\Personal\\Python Examples")

#print (os.getcwd())

#pattern = re.compile(r'J[a-z]+\sJ[a-zA-Z]+')
pattern = re.compile(r'\d{3}\s(H[a-z]+\s\w+\.),\s(\w+\s\w+\s\w+)') # here i grouped them with '()' so i can extract how i wants but result will be same

with open ("data.txt", 'r+') as f:
    data = f.read()
    #print (data)

    matches = pattern.finditer(data)
    #print (matches)
    for match in matches:
        print (match.group()) #written only strips not other "_sre.SRE_Match object; span=(4, 11)" stuff..
        print (match.group(2))
        #print (match.span()) --> written index of find iter strings

    

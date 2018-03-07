array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
#print (array)

li = [1,2,3,4,2,4,5,6,2,56,7,34,5,457,6,5]

def func(a, *b): # '*b' takes multiple argument and kept in tuple
    print (a,b) # O/P --> 3 (4,4,5,6,7)

ab = 3

func(ab, 4, 4, 5, 6, 7)

import time

print (time.localtime())
# o/p --> time.struct_time(tm_year=2018, tm_mon=2, tm_mday=13, tm_hour=13, tm_min=35, tm_sec=3, tm_wday=1, tm_yday=44, tm_isdst=0)

print (time.localtime()[7])

import calendar

#print (calendar.__dir__())
print (calendar.month(1992, 2))


newDict = {1:"One", 3:"Three", 5:"Five", 7:"Seven", 9:"Nine"}

new1 = newDict.copy()
new1.setdefault(10, 'Ten')
print (new1, newDict)
li1 =li.copy()
li1.append(3)
print (li1, li)

hemanth = "Hemanth"

print (hemanth)

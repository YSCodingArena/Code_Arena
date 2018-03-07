s1 = list('otfnwkedo')
s2 = list('fjothurwao')#jha

dictList = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight':8, 'nine':9}

for val in dictList.keys():
    flag = True
    i=0
    for i in val:
        if i in s2:
            continue
        else:
            flag = False
            break
    if flag:
        print (dictList[val], end = "")
        [s2.remove(n) for n in val]


######################################################################

        
str1 = 'axxxxyyyyxxab'

def recurFunc(val):
    for a in str1:
        

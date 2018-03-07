#Sorting the keys

dictList = {2:"two", 4:"four", 3:"Three",1: "One"}

keys = list(dictList.keys())

sortedKeys = sorted(keys)
for key in sortedKeys:
    #print (key, dictList[key])
    pass

newDict = {"two":2, "four":4, "Three":3, "One":1}

val = list(newDict.items())
for i in range(len(val)):
    for i in range(len(val)):
        if i < len(val)-1:
            if val[i][1] > val[i+1][1]:
                val[i], val[i+1] = val[i+1], val[i]
            
print (val)





#This is another solution
'''
import operator
sorted_x = sorted(newDict.items(), key=operator.itemgetter(1))
print (sorted_x)

'''

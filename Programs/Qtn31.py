from timeit import Timer
t = Timer("for i in range(100):1+1")
print (t.timeit())


#____________________________________________________
'''
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print (sentence)


#or another solution

print ("\n".join(["%s %s %s." % (subjects[i], verbs[j], objects[k]) for i in range(len(subjects)) for j in range(len(verbs)) for k in range(len(objects))]))



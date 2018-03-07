'''
Printing the pyramid of numbers
'''

lvl = input("What is the pyramid level, like 1 or 2 :")

level = eval(lvl)

#===============================================================================
# for i in range(1, level+1):
#     for j in range(i):
#         print (i, end = "")
#         
#     print ()
#
#Output:
# 1
# 22
# 333
# 4444
# 55555
#===============================================================================
list_num = []
for i in range(1, level+1):
    num = level - i
    while num > 0:
        print (end = " ")
        num -= 1
        
    for j in range(1, i+1):
        print (j, end = "")
    
    print ("".join([str(i) for i in list_num])) 
    list_num = [i for i in range(1,i+1)]
    list_num = list_num[::-1]
         
    print ()
    #list_num = []
    
    
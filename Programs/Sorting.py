list_num = [1, 21, 1581, 51, 51, 5, 135, 1, 186, 1, 3581, 681, 68, 13, 20, 2, 85, 1056, 1, 65, 65, 685, 0, 3, 8, 21, 381, 51, 2]

#Solution #1 
 for i in range(len(list_num)):
     for j in range(len(list_num)-1):
         if list_num[j] > list_num[j+1]:
             list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
             
 print (list_num)

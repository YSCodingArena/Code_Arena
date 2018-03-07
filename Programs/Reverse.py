a = 'Hemanth Kumar Y S'
b = [i for i in a if i != " "]

#print (a, b)

reversed_num = [a[-i] for i in range(1, len(a) + 1)]

print ("".join(reversed_num))  

c = a.split(" ")

print (c)

reverse_num = [i[-j] for j in [i for i in c]]

print (reverse_num)
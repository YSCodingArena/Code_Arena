#Input = I AM HEMANTH
#Output = I MA 
#===============================================================================
# 
# str1 = "I AM HEMANTH"
# temp1 = ""
# temp2 =[]
# for j,i in enumerate(str1):
#     if i == " " or j == len(str1)-1:
#         temp1 = temp1 + i
#         temp1 = temp1[::-1]
#         temp2.append(temp1.strip())
#         temp1 = ""
#     temp1 = temp1 + i
# print " ".join(temp2)
#===============================================================================

#Input = I AM HEMANTH
#output = HTNAMEH MA I

str1 = "I AM HEMANTH"
temp1 = ""
temp2 =[]
for j,i in enumerate(str1):
    if i == " " or j == len(str1)-1:
        temp1 = temp1 + i
        temp1 = temp1[::-1]
        temp2.append(temp1.strip())
        temp1 = ""
    temp1 = temp1 + i
  
temp2 = temp2[::-1] 
print (" ".join(temp2))

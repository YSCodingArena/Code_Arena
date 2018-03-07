#===============================================================================
# import os
# 
# path = input("Enter the path here : ")
# fileCount = 0
# for root, folder, files in os.walk(path):
#     #fileCount+=len(files)
#     #print (root)
#     for file in files:
#         fileName = file.split(".")[0] + ".jpg"
#         #os.path.join(root, fileName)
#         #print (fileName, file)
#         os.rename(os.path.join(root, file), os.path.join(root, fileName))
# print ("Done BOSS!!")
# print ("I'm Mad Genius!!")
#===============================================================================


try:
    print ("Kulli kavya!!")
    raise NameError("Kavya!!")
except Exception as error:
    print ("Error: ", error)

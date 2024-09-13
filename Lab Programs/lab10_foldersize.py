# import module
import os
 
# assign size
size = 0
 
# assign folder path
Folderpath = 'c:\\Users\\k3bywp8'   
 
# get size
for ele in os.scandir(Folderpath):
    print(ele)
    size+=os.path.getsize(ele)
     
print(size)
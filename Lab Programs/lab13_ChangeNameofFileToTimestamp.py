import os
import time

file_path = 'c:\\Users\\k3bywp8\\text1.txt'

creation_time = os.path.getctime(file_path)
print(f"File Creation Time is: {creation_time}")
creation_time = time.ctime(creation_time)              # Covert to time stamp

print(type(creation_time))
creation_time = time.strptime(creation_time)           # Convert String(str) time format
print(type(creation_time))

creation_time = time.strftime("%Y-%m-%d %H:%M:%S", creation_time)
print(f"File Creation Time is: {creation_time}")

creation_time = creation_time.replace(":", "_").replace(" ","_") 
print(f"File Creation Time is: {creation_time}")

print(os.path.split(file_path)[0])
print(os.path.split(file_path)[1])

os.rename(file_path, os.path.split(file_path)[0]+creation_time+".txt")
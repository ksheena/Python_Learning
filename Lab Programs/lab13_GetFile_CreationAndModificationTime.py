import os
import time

file_path = 'c:\\Users\\k3bywp8\\Book1.csv'

creation_time = os.path.getctime(file_path)
modified_time = os.path.getmtime(file_path)


print(f"File Creation Time is: {creation_time}")
print(f"File Modification Time is: {modified_time}")

creation_time = time.ctime(creation_time)              # Covert to time stamp
modified_time = time.ctime(modified_time)
print(f"File Creation Time is: {creation_time}")
print(f"File Modification Time is: {modified_time}")
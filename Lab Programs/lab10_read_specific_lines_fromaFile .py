import os


path = 'c:\\Users\\k3bywp8\\text3.txt'

file_stats = os.stat(path)
id = file_stats.st_ino

print(f"File ID is: {id}")
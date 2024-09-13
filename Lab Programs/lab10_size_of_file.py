import os


file_name = 'c:\\Users\\k3bywp8\\NTUSER.DAT'
file_stat = os.path.getsize(file_name)

print(f'Size of file is: {(file_stat/1024)/1024} MB')

file_st = os.stat(file_name)
print(f'Size of file is: {(file_st.st_size/1024)/1024} MB')
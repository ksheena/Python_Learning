import os

dir = "c:\\Users\\k3bywp8\\python"

large_file_path = ""
large_file_szie = 0

for root, dirs, files in os.walk(dir):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        if file_size > large_file_szie:
            large_file_szie = file_size
    large_file_path = file_path


print(f"Large File path: {large_file_path}  :: File Size {large_file_szie}")
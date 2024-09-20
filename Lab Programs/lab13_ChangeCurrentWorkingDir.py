import os

print(f"Current Working Directory is : {os.getcwd()}")

new_dir = input("Enter New Working Directory: ")

os.chdir(new_dir)

print(f"Current Working Directory Chnaged to : {os.getcwd()}")
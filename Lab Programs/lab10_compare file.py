from difflib import Differ 
  
with open('c:\\Users\\k3bywp8\\text4.txt') as file_1, open('c:\\Users\\k3bywp8\\text5.txt') as file_2: 
    differ = Differ() 
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()): 
        print(line) 
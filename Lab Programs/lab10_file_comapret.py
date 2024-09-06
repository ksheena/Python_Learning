import filecmp

file1 ='c:\\Users\\k3bywp8\\text1.txt'
file2 =  'c:\\Users\\k3bywp8\\text2.txt'
result = filecmp.cmp(file1, file2, shallow=False)
print(result)


with open(file1, 'r') as f1, open(file2, 'r') as f2:
    if f1.read() == f2.read():
        print("files are matching")
    else:
        print("files not are matching")

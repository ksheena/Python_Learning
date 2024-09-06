
line_cnt = 0
line_cnt2 = 0
fo=open('c:\\Users\\k3bywp8\\text1.txt','r') 
for line in fo.read():
    word = line.split()
    line_cnt +=len(word)

print(line_cnt)

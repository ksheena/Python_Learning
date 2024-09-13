fo=open('c:\\Users\\k3bywp8\\text1.txt','r') 
text1_content = fo.read()
fo.close()

print(text1_content)

fo=open('c:\\Users\\k3bywp8\\text2.txt','w') 
fo.write(text1_content)
fo.close()

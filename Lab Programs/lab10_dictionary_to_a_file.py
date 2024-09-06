mydict = {'fname' : "kiran", 'lname' : "kumar", 'dep' : "ACDC"}


fo=open('c:\\Users\\k3bywp8\\text3.txt','w') 
for key, value in mydict.items():
    fo.write('%s:%s\n' % (key, value))


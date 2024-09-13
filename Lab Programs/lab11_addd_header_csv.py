import pandas as pd


header_list = ['id','name','count','weeks']

file = pd.read_csv('c:\\Users\\k3bywp8\\Book1.csv')

#file.columns = header_list
#file.to_csv('c:\\Users\\k3bywp8\\Book1.csv', index=False)

file.to_csv("c:\\Users\\k3bywp8\\Book1.csv", header=header_list, index=False) 

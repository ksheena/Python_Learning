import pandas as pd


header_list = ['id','name','count','weeks']

file = pd.read_csv('c:\\Users\\k3bywp8\\Book1.csv')

print(file.columns)
import pandas as pd

file = pd.read_csv('c:\\Users\\k3bywp8\\Book1.csv')
file.loc[2, 'name'] ="Kiran Kumar"

file.to_csv('c:\\Users\\k3bywp8\\Book1.csv')

print(file)
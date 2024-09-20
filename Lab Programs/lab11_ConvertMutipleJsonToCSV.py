# Crate json file file1.json and file2.json 
#file1.json and file2.json
'''
{
    "ID":{
        "0":01,
        "1":02
        },
    "Name":{
        "0":"Kiran",
        "1":"Kumar"
        },
    "Department":{
        "0":"ACDC",
        "1":"ACDC"
        }
}
'''

import pandas as pd

f0 = pd.read_json('c:\\Users\\k3bywp8\\file1.json')
f1 = pd.read_json('c:\\Users\\k3bywp8\\file2.json')

df = pd.concat([f0,f1])                # concatinate two files

df.to_csv('c:\\Users\\k3bywp8\\result.csv', index=False)

data = pd.read_csv('c:\\Users\\k3bywp8\\result.csv')

print(data)

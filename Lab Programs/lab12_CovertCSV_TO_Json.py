# create CSV file
import pandas as pd
import json

df = pd.read_csv('c:\\Users\\k3bywp8\\result.csv')        # read csv
df.to_json('c:\\Users\\k3bywp8\\result2.json')             # Convert to json       


with open('c:\\Users\\k3bywp8\\result2.json', 'r') as file:       # Read content of json
    data = json.load(file)

print(data)
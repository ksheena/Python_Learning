import csv


content = [['Fame','Lanme','Department'],['Kiran','Sheena','ACDC'], ['Kiran','Kumar','ACDC']]

with open('c:\\Users\\k3bywp8\\Book2.csv', mode='w', newline='') as file:
    writer= csv.writer(file)
    for line in content:
        writer.writerow(line)

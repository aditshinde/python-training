import csv

data = [
    ('ID','Title','Author'),
    ('1','CRLS','Cormen'),
    ('2','C for Dummies','Rayson'),
    ]

with open('AllBooks.csv','w') as outFile:
    csv_writer = csv.writer(outFile)
    for row in data:
        csv_writer.writerow(row)

with open('AllBooks.csv','r') as inFile:
    csvIterable = csv.reader(inFile)
    for row in csvIterable:
        print(row)
"""
1. Csv module
2 reader and writer objects
"""
import csv

with open("contacts.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)


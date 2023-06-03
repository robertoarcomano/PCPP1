"""
1 Csv module
2 open the file
3 use reader object
4 use DictReader to read every line as dictionary
5 use list(DictReader) to create a list of dictionaries
6 use fieldnames to specify the fields names
7 use writer objects
8 specify quotechar
9 use DictWriter

"""
import csv

print("Using csv.reader")
with open("contacts.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)

print("\nUsing csv.DictReader")
with open("contacts.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    print(list(reader))

print("\nUsing manual fields list")
with open("contacts1.csv") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["First", "Second"])
    print(list(reader))

print("\nWriting to file")
with open("contacts2.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["ID", "Name"])
    for i in range(1,10):
        writer.writerow([str(i), "Roberto," + str(i)])

print("\nWriting to file using a Dictionary")
with open("contacts3.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["ID", "NAME"])
    writer.writeheader()
    for i in range(1,10):
        writer.writerow({"ID": str(i), "NAME": "Roberto_" + str(i)})


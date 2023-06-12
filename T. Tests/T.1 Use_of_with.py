i = 0
with open("T.1 Use_of_with.py", "r") as textfile:
    for line in textfile:
        print(i, line)
        print(textfile.closed)
        i += 1

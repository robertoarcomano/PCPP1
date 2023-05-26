i = 0
with open("c:\\text.txt", "r") as textfile:
    for line in textfile:
        print(i, line)
        i += 1

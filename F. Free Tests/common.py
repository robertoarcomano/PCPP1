def title(string, *args):
    def header():
        title_char = "#"
        title_char_number = 3
        for h in range(title_char_number):
            print(title_char, end="")

    header()
    print(" " + string, end=" ")
    header()
    print()
    for arg in args:
        print(arg)
    if args:
        print()

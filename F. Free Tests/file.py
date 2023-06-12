def remove_lf(string):
    return string.replace("\n", "")


def replace_quotes(string):
    return string.replace("\"", "'")


def all_replaces(string):
    return remove_lf(replace_quotes(string))


def read_and_format_file(filename):
    with open("file.py", "r") as my_file:
        return list(map(all_replaces, my_file.readlines()))


for item in read_and_format_file("file.py"):
    print(item)


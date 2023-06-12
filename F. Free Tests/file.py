def remove_lf(string):
    return string.replace("\n", "")


def replace_quotes(string):
    return string.replace("\"", "'")


def all_replaces(string):
    return remove_lf(replace_quotes(string))


def show(my_list):
    for item in my_list:
        print(item)


my_file = open("file.py", "r")
my_data1 = my_file.readlines()
my_file.close()

my_data3 = list(map(all_replaces, my_data1))
show(my_data1)
show(my_data3)


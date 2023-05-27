"""
1 JSON = JavaScript Object Notation
2 UTF-8 coded text
3 Numbers:
    3.1 3.141592653589
    3.2 3.0857E16
    3.3 −1.6021766208E−19
4 Boolean:
    4.1 false
    4.2 true
5 Null:
    5.1 null
6 Objects: {}
    6.1 "name":
    6.2 value or "value" if it is a string
7 Arrays: []
8 Separator: ,
9 Empty object: {}

"""
import json

my_variable = {
    "name": "Roberto",
    "arr": [1, 2, 3],
    "bool": False,
    "null": None
}

# From dict to json text
my_text_json = json.dumps(my_variable)
print(my_text_json, type(my_text_json))

# From json text to dict
my_new_variable = json.loads(my_text_json)
print(my_new_variable, type(my_new_variable))



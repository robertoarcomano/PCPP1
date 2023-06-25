"""
1 Coding convention (code style guide)
2 Our code will be read much more often than it will be written
3 Tools:
    3.1 pycodestyle
    3.2 autopep8
    3.3 PEP 8 online
4 Indentation: 4 spaces (no tabs)
5 Continuation lines: (opening argument functions)
6 Max line length: Max 79 (maybe 99 if requested) chars, 72 for docstrings and comments
7 Line breaks: break before operations
8 Blank Lines (vertical whitespaces)
    8.1 2 blank lines to surround top level fn and classes
    8.2 1 black line to surround method definition
    8.3 blank lines in functions to indicate logical sections
9 Default encodings: UTF-8
10 Imports at the beginning of the script
    10.1 Standard library imports;
    10.2 Related third-party imports;
    10.3 Local application/library specific imports.
    10.4 At least 1 blank line between groups of imports
    10.5 Import in separated lines
    10.6 Absolute imports
    10.7 avoid using wildcard imports
11 Quotes:
    11.1 Single and double are the same
    11.2 They can mutually be used to escape characters
12 Whitespaces:
    12.1 Do not use unnecessary white spaces
    12.2 No space with colon slice
    12.3 not use excessive whitespace
    12.4 Not more than 1 space around operators
    12.5 One space around binary operators (+=)
    12.6 Do not use space with "=" when it specifies a default argument
13 Comments:
    13.1 Use self-commenting code
    13.2 Coherence
    13.3 Complete sentences comment (This is a comment.)
    13.4 2 spaces between sentences
    13.5 Block comments:
        13.5.1 The code just follows the comment
        13.5.2 Same indentation as the code
    13.6 Inline comments:
        13.6.1 Same line as the code
        13.6.2 Add at least 2 whitespaces
        13.6.3 Never tell obvious or unnecessary things
        13.6.4 Self-commenting code is better than any comments
    13.7 Documentation Strings (docstrings) """"""
14 Naming conventions
    14.1 Naming styles
        14.1.1 Do not use l I O because they can be confused with 0 and 1
        14.1.2 Snake_case: underscore instead of whitespace
        14.1.3 CamelCase
        14.1.4 Acronym in capital: HTTPServerError
        14.1.5 myMixedCase
        14.1.6 My_Snake_Camel_Case
        14.1.7 _internal_use (not imported)
        14.1.8 class_ to avoid conflicts with Python reserved keywords
        14.1.9 __my_name_mangling
        14.1.10 __my_var__ is used for magic in a controlled namespace
    14.2 Recommendations
        14.2.1 my_variable
        14.2.2 my_function
        14.2.3 MyClass
        14.2.4 my_class_method
        14.2.5 self for instance methods
        14.2.6 cls for class methods
        14.2.7 MY_CONSTANT
        14.2.8 my_module.py
        14.2.9 mypackage
        14.2.10 MyType
        14.2.11 MyException
        14.2.12 
15 Programming recommendations
    15.1 a is None
    15.2 if a is True or better if a
    15.3 "not a is None" becomes "a is not None"
    15.4 Use "if x is not None" instead "if x"
    15.5 Specialize exceptions checking
    15.6 Use ''.startswith() and ''.endswith() for prefixes and suffixes
    15.7 Use String methods
    15.8 
"""
import os
import sys
from os import sync
var1 = {
    "a": 1,
    "b": "2"
}
var2 = (1
        + 2
        - 3)


class MyClass1:
    pass


class MyClass2:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def fn1():
    print("start")

    # Doing something
    # Working on something

    print("end")


print("ok")
a = [1, 2, 3]
b = a[:]
c = 1 + 2
c += 1

if a == 0:
    # This is a comment.
    pass
    # This is a multi-line comment. Line 1
    #
    # Line 2

a = 1  # This is an inline comment.

"""
This is a example of documentation strings, docstrings
"""
""" This is another example of documentation strings, docstrings """

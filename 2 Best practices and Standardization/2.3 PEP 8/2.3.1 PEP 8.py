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

"""
1 __doc__ special attribute or help() function
2 Docstring are used for documenting the code
3 Comments to increase code readability
4 Comments are to be used for:
    4.1 Code and algorithm descriptions
    4.2 # TODO:
    4.3 Testing
    4.4 Planning
5. PEP 484 Type Hinting
    5.1 Alternative to comments
    5.2 It statically indicates type information
    5.3 After parameter and as return type
    5.4 Optional
    5.5 not used at runtime
6. Docstrings

"""


def hello(name: str) -> str:
    return "Hello, " + name

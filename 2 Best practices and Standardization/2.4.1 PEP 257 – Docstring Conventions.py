"""
1 __doc__ special attribute or help() function
2 Docstring are used for documenting the code
3 Comments to increase code readability
4 Comments are to be used for:
    4.1 Code and algorithm descriptions
    4.2 # TODO:
    4.3 Testing
    4.4 Planning
5 PEP 484 Type Hinting
    5.1 Alternative to comments
    5.2 It statically indicates type information
    5.3 After parameter and as return type
    5.4 Optional
    5.5 not used at runtime
6 Docstrings
    6.1 They should be used
    6.2 Just for public methods
    6.3 They are in the first statement of a module
    6.4 Can be extracted with docutils
    6.5 2 types:
        6.5.1 Attribute docstrings, immediately after an assignment
        6.5.2 Additional docstrings, immediately after another docstring
    6.6 One-line docstrings for short descriptions
    6.7 Multi-line docstrings for more difficult cases
    6.8 A docstring should prescribe the code segment's effect, not describe it
        (do this, return this...)
    6.9 Not just function name and parameters
    6.10 No blank lines
    6.11 Focused on "What" and not on "How"?
    6.12 Multi-line Docstrings
        6.12.1 Same indentation as the code
        6.12.2 2 blank lines after all docstrings
    6.13 Script, module, package docstrings documents all the features of them
    6.14 Function and class docstrings should summarise their behaviour
    6.15 Formatting types:
        6.16 reStructuredText
        6.17 NumPy/SciPy
        6.18 Use can use Sphinx tool to generate documentation
7 General documentation:
    7.1 Readme for brief information, purpose and installation guidelines
    7.2 Examples.py, for how to use it
    7.3 License
    7.4 How to contribute
8 Try using automated tools
    8.1 Sphinx
    8.2 Pdoc
9 Linters and fixers (IDE)
10 Use object.__doc__ to show the docstrings
"""


def hello(name: str) -> str:
    return "Hello, " + name


def my_function():
    """I am a docstring."""


print("help(print)")
print(help(print))
print("print.__doc__")
print(print.__doc__)


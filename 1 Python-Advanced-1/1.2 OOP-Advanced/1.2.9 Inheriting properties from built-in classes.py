"""
1. It is useful to extend a build-in Python class and make some changes
2. Ex: list which accepts integer only or str that accepts maximum 10 chars
    2.1 Extend str class
    2.2 Override __init__
"""
class Mystring10(str):
    def __new__(cls, string):
        if len(string) > 10:
            raise ValueError("String too long")
        return super(Mystring10, cls).__new__(cls, string)

str1 = Mystring10("12345678901")
print(str1)

"""
1. All exceptions come from BaseException: 63
2. Unnamed/anonymous exceptions: except ZeroDivisionError
3. Name exception
    3.1 Example: except ImportError as e
    3.2 Not all exceptions provide additional data
4. Chained Exceptions
    4.1 Implicit: you don't want to lose an exception just because another one was raised: __context__ attribute
    4.2 Explicit: Voluntarily translation from one Exception to another one: __cause__ attribute
5. Nested message: During handling of the above exception, another exception occurred
6. You can use "is" operator to check the equivalence of 2 objects
7. __context__ keeps trace of all nested exceptions launched so far
8. Always try to specify the most specialised exception
9. __cause__ can go back from a "raise" to the previous exception launched
10. Every exception has the __traceback__ attribute to see the track of the exception
    10.1 We can use format_tb() to retrieve all entries
    10.2 We can use print_tb() to print all entries directly to stdout
"""
class MyClassException(Exception):
    pass
class MyClass:
    def __init__(self, n):
        self.n = n
    def division(self, m):
        d = 1
        try:
            d = self.n / m
        except ZeroDivisionError:
            pass
        return d
    @staticmethod
    def fake_import():
        try:
            import xxx
        except ImportError as e:
            print(e)
    @staticmethod
    def fake_decode():
        try:
            b'\x80'.decode("utf-8")
        except UnicodeError as e:
            print(e)
            print("encoding: " + e.encoding)
            print(e.reason)
            print(e.object)
            print(e.start)
            print(e.end)
    @staticmethod
    def nested_exceptions():
        mylist = [0,1]
        try:
            print(mylist[2])
        except BaseException:
            try:
                import xxx
            except ImportError as second:
                try:
                    print(0/0)
                except ZeroDivisionError as third:
                    print("third exception:",third)
                    print("second exception:",second)
                    print("third.__context__ is second",third.__context__ is second)
                    print("first exception(second.__context__):",second.__context__)
    @staticmethod
    def explicit_exception_raise():
        mylist = [0,1]
        try:
            print(mylist[2])
        except IndexError as e:
            raise MyClassException("Problem with bounds") from e


myclass1 = MyClass(10)
print(myclass1.division(0))
myclass1.fake_import()
myclass1.fake_decode()
myclass1.nested_exceptions()
print()
try:
    myclass1.explicit_exception_raise()
except MyClassException as f:
    print(f, "caused by", f.__cause__)
    print(f.__traceback__)
    import traceback
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))
    traceback.print_tb(f.__traceback__)

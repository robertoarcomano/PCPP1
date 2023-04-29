class Myclass:
    def __init__(self, n):

        self.n = n
    def __add__(self, obj):
        return self.n + obj.n
    def __iadd__(self, obj):
        self.n = self.n + obj.n
        return self
    def __getattr__(self, attribute):
        return attribute;
    def __getattribute__(self, attribute):
        return super().__getattribute__(attribute) + 0;

myclass1 = Myclass(1)
print("myclass1.n:",myclass1.n)

myclass2 = Myclass(2)
print("myclass2.n:",myclass2.n)
print()

print("myclass1 + myclass2:",myclass1 + myclass2)
print()

myclass1 += myclass2
print("myclass1 += myclass2")
print("myclass1.n:", myclass1.n)
print()

print("myclass1.not_existing_attribute:", myclass1.not_existing_attribute)
print()

print("isinstance(myclass1,object):", isinstance(myclass1,object))
print()

print("issubclass(Myclass,object):", issubclass(Myclass,object))
print()

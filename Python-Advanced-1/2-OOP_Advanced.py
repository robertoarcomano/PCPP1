class Myclass:
    def __init__(self, n):

        self.n = n
    def __add__(self, obj):
        return self.n + obj.n
    def __iadd__(self, obj):
        self.n = self.n + obj.n
        return self
    # def __getattribute__(self, attribute):
    #     print(attribute)
    #     # if attribute == "what-is-my-attribute":
    #     #     return self.n

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



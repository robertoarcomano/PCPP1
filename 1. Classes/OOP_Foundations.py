class Myclass:
    static_var = "static"

    def __init__(self):
        static_var = "local_var"

        print("static_var:", static_var)
        print("self.static_var:", self.static_var)
        print("Myclass.static_var:", Myclass.static_var)

        self.static_var = "dynamic1"

        print("static_var:", static_var)
        print("self.static_var:", self.static_var)
        print("Myclass.static_var:", Myclass.static_var)

        print()


i1 = Myclass()
i2 = Myclass()

print(Myclass.static_var)
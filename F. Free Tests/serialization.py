from common import title
import pickle


class MyClass:
    def __init__(self, name):
        self.name = name


my_obj = MyClass("my_obj")

with open("my_obj.data", "wb") as file:
    pickle.dump(my_obj, file)

with open("my_obj.data", "rb") as file:
    title("load from file:", pickle.load(file).__dict__)

with open("my_byte_array_obj.data", "wb") as file:
    my_byte_array = pickle.dumps(my_obj)
    file.write(my_byte_array)

with open("my_byte_array_obj.data", "rb") as file:
    my_byte_array = pickle.dumps(my_obj)
    my_byte_array = file.read(len(my_byte_array))
    title("load byte array from file:", pickle.loads(my_byte_array).__dict__)

import to_import as my_module
import to_import
from to_import import var, fn, MyClass

print(my_module.var, my_module.MyClass("my_object1").get_name(), my_module.fn())
print(to_import.var, to_import.MyClass("my_object2").get_name(), to_import.fn())
print(var, MyClass("my_object1").get_name(), fn())

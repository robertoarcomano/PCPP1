import module1 as my_module
import module1
from module1 import var1, fn1, MyClass1
from pkg1 import module2

print(my_module.var1, my_module.MyClass1("my_object").get_name(), my_module.fn1())
print(module1.var1, module1.MyClass1("my_object").get_name(), module1.fn1())
print(var1, MyClass1("my_object").get_name(), fn1())
print(module2.var2, module2.MyClass2("my_object").get_name(), module2.fn2())

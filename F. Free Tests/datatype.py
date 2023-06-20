from common import title

my_list = [1, 2, 3, 3]
title("my_list", my_list)
print("my_list.append(4)")
my_list.append(4)
title("my_list", my_list)

my_tuple = 1, 2, 3, 3, "Hello!", [10, 20, 30]
title("my_tuple", my_tuple)

title("my_tuple[5]", my_tuple[5])
print("my_tuple[5][0] = 4")
my_tuple[5][0] = 4
title("my_tuple[5]", my_tuple[5])
title("my_tuple", my_tuple)

print("s = set(my_list)")
s = set(my_list)
title("s", s)
print("s.add(2)")
s.add(2)
title("s", s)
print("s.add(5)")
s.add(5)
title("s", s)
print("s.pop()")
s.pop()
title("s", s)

print("f = frozenset(s.union((9,)))")
f = frozenset(s.union((9,)))
title("f")
for i in f:
    print(i, end=" ")
print()
print("f.issuperset(s):", f.issuperset(s))
print()

print("c = complex(1, 2)")
c = complex(1, 2)
title("c", c)

print("r = range(10, 0, -1)")
r = range(10, 0, -1)
title("r")
for i in r:
    print(i, end=" ")

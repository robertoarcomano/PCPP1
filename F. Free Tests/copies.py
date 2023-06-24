from common import title
import copy

a = {"id": 1, "name": "ok"}
b = {"id": 1, "name": "ok"}
c = a

title("id(a)", id(a))
title("id(b)", id(b))
title("id(c)", id(c))
title("a == b", a == b)
title("a is b", a is b)
title("c is a", c is a)

print()
a = {
    "a": ["1", "2"],
    "b": {
        "c": ["3", "4"]
    }
}
d = copy.copy(a)
e = copy.deepcopy(a)
title("d == a", d == a)
title("e == a", e == a)
title("d is a", d is a)
title("e is a", e is a)

title("d['a'] is a['a']", d['a'] is a['a'])
title("e['a'] is a['a']", e['a'] is a['a'])

from common import title


def fn(a, b, c, d=1, *args, **kwargs):
    return \
        "a:", a, \
            "b:", b, \
            "c:", c, \
            "d:", d, \
            "args:", args, \
            "kwargs:", kwargs


title("fn(1,2,3)", fn(1, 2, 3))
title("fn(1,2,3,5)", fn(1, 2, 3, 5))
title("fn(1,2,3,5,6,7,8, var1=9, var2=10)", fn(1, 2, 3, 5, 6, 7, 8, var1=9, var2=10))

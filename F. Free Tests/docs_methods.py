def text(value, print_needed=True):
    global text_number
    print(str(text_number), value)
    if print_needed:
        print(eval(value))
    else:
        eval(value)
    print()
    text_number += 1


def fn(a=True):
    """fn function"""
    pass


text_number = 1
text("fn.__doc__")
text("help(fn)", False)
text("dir()")

fn()

"""
1 Access a property like a dictionary: object["property"]
2 widget.cget("name")
3 widget.config(name=value)
4 font: ("font_family_name", "font_size", "font_style")
5 Size:
    5.1 borderwidth	The width of the 3D-frame surrounding some widgets (e.g., Button)
    5.2 highlightthickness	The width of the additional frame drawn around the widget when it gains the focus
    5.3 padx/pady	The width/height of an additional empty space/margin around the widget
    5.4 wraplength	If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
    5.5 height	The height of the widget
    5.6 underline	The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback to work – no automation here, sorry)
    5.7 width	The width of the widget
6 Color change:
    6.1 background/bg	The color of the widget’s background (you can freely use either of these two forms)
    6.2 foreground/fg	The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)
    6.3 activeforeground/activebackground	Like bg and fg but used when the widget becomes active
    6.4 disabledforeground	The width of the widget
7 Anchor (alignment) N S O E + Center
8 Mouse cursor:

"""

import tkinter as tk

def change_label():
    my_label["text"] += "1"
    my_label.config(text=my_label.cget("text")+"0")
def change_font():
    font = my_label.cget("font")
    print(font)
    my_label["font"] = ("Arial", "12", "bold")
def change_size():
    print(type(my_label["borderwidth"]))
    my_label["borderwidth"] = 10
def change_color():
    print(type(my_label["bg"]))
    my_label["bg"] = "lightblue"
def change_anchor():
    print(my_label["anchor"])
    my_label["anchor"] = tk.W
    my_label["width"] = 20
    print(my_label["anchor"])


my_window = tk.Tk()
# my_window.geometry("640x480")
my_label = tk.Label(my_window, text="my label")
my_label.pack()
my_button = tk.Button(my_window, text="change label", command=change_label)
my_button.pack()
my_font_button = tk.Button(my_window, text="change font", command=change_font)
my_font_button.pack()
my_size_button = tk.Button(my_window, text="change size", command=change_size)
my_size_button.pack()
my_color_button = tk.Button(my_window, text="change color", command=change_color)
my_color_button.pack()
my_anchor_button = tk.Button(my_window, text="change anchor", command=change_anchor, cursor="clock")
my_anchor_button.pack()


my_window.mainloop()
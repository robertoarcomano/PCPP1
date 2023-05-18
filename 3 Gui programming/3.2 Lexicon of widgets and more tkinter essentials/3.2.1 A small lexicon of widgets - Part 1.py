"""
1 Widget constructor(master, option...)
2 master can be:
    2.1 window
    2.2 frame
    2.3 labelframe
3 Widgets can be:
    3.1 clickable
    3.2 non-clickable
4 Button: command, justify, state(active, disable)
5 Checkbutton:
    5.1 Attributes: bd (width), command, justify, state, variable (0,1), offvalue, onvalue
    5.2 Methods: deselect(), flash(), invoke(), select(), toggle()
6 Radiobutton:
    6.1 Attributes: command, justify, state, variable (0,1), value
    6.2 Methods: deselect(), flash(), invoke(), select()
"""
import tkinter as tk


def clicked():
    print("clicked")


def enable_it():
    my_button["state"] = tk.ACTIVE


def disable_it():
    my_button["state"] = tk.DISABLED


def toggle():
    if my_button["state"] != tk.DISABLED:
        my_button["state"] = tk.DISABLED
    else:
        my_button["state"] = tk.ACTIVE


def checkbutton_variable_observer(id, idx, act):
    print(my_checkbutton_variable.get())
    if my_checkbutton_variable.get():
        my_button["state"] = tk.ACTIVE
    else:
        my_button["state"] = tk.DISABLED


def onmouseover(event):
    print("onmouseover")


def onmouseout(event):
    print("onmouseout")


def my_radiobutton1_cmd():
    my_checkbutton_variable.set(my_radiobutton1_var.get())


my_window = tk.Tk()

my_button = tk.Button(my_window, text="OK", command=clicked)
my_button.pack()
my_button.bind("<Enter>", onmouseover)
my_button.bind("<Leave>", onmouseout)

my_toggle = tk.Button(my_window, text="Button Toggle", command=toggle)
my_toggle.pack()

my_checkbutton_variable = tk.IntVar()
my_checkbutton_variable.set(1)
my_checkbutton = tk.Checkbutton(my_window, text="Check Toggle", variable=my_checkbutton_variable)
my_checkbutton_variable.trace("w", checkbutton_variable_observer)
my_checkbutton.pack()

my_radiobutton1_var = tk.IntVar()
my_radiobutton1_var.set(1)
my_radiobutton11 = tk.Radiobutton(my_window, text="botton active", variable=my_radiobutton1_var, value=1, command=my_radiobutton1_cmd)
my_radiobutton11.pack()
my_radiobutton12 = tk.Radiobutton(my_window, text="botton disabled", variable=my_radiobutton1_var, value=0, command=my_radiobutton1_cmd)
my_radiobutton12.pack()

my_window.mainloop()

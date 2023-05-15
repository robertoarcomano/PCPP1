"""
1 Messagebox.showinfo(title, info)
2 When "command" is not available you can use bind(event, callback) callback is called with 1 event parameter
3 Event properties:
    3.1 x, y: coordinates related to the clicked widget
    3.2 x_root, y_root: coordinates related to the screen
    3.3 char, keysym, keycode: key pressed char, symbol and code
    3.4 num: number of clicks
4 Set a widget property: widget.config(property=value) -> also to unbind an event
5 Bind_all(event, callback) / unbind_all(event)
"""
import tkinter as tk
import tkinter.messagebox as messagebox

def ok_clicked(event=None):
    messagebox.showinfo("Info", "You clicked ok!")
def label_clicked(event=None):
    print("label clicked!", event)
def switch_label_clicked(event=None):
    my_var = my_check_variable.get()
    print("switch! Variable:", my_var)
    if my_var == 1:
        my_label.bind("<Button-1>", label_clicked)
    else:
        my_label.unbind("<Button-1>")
def switch_button_clicked(event=None):
    my_var = my_button_variable.get()
    print("switch1! Variable:", my_var)
    if my_var == 1:
        my_button.bind("<Button-1>", ok_clicked)
    else:
        my_button.unbind("<Button-1>")
def switch_bind_all_clicked(event=None):
    my_var = my_bind_all_variable.get()
    print("switch bind_all! Variable:", my_var)
    if my_var == 1:
        my_window.bind_all("<Button-1>", ok_clicked)
    else:
        my_window.unbind_all("<Button-1>")
my_window = tk.Tk()
my_window.geometry("640x480")

my_button = tk.Button(my_window, text="OK")
my_button.pack()

my_check_variable = tk.IntVar()
my_check_variable.set(0)
my_button_variable = tk.IntVar()
my_button_variable.set(1)
my_bind_all_variable = tk.IntVar()
my_bind_all_variable.set(0)

my_checkbutton = tk.Checkbutton(my_window, text="Swap Label", command=switch_label_clicked, variable=my_check_variable)
my_checkbutton.pack()
my_checkbutton1 = tk.Checkbutton(my_window, text="Swap Button", command=switch_button_clicked, variable=my_button_variable)
my_checkbutton1.pack()
my_checkbutton2 = tk.Checkbutton(my_window, text="Swap bind_all", command=switch_bind_all_clicked, variable=my_bind_all_variable)
my_checkbutton2.pack()
my_label = tk.Label(my_window, text="Hello!")
my_label.pack()

switch_label_clicked()
switch_button_clicked()
my_window.mainloop()
"""
1 Label (text="")
2 Frame (height="", width="")
3 Variable (IntVar(), set())
4 Checkbutton (text, variable)
5 Entry
6 Radiobutton (text, variable, value)
"""
import tkinter as tk
my_window = tk.Tk()

my_label = tk.Label(my_window, text="My Label")
my_label.pack()

my_frame = tk.Frame(my_window, height=200, width=200, bg="green")
my_frame.pack()

my_button = tk.Button(my_window, text="OK")
my_button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

def show_switch():
    print(switch.get())
my_check_button = tk.Checkbutton(my_window, text="Check 1", variable=switch, command=show_switch)
my_check_button.pack()

my_entry = tk.Entry(my_window)
my_entry.pack()

my_radio_button1 = tk.Radiobutton(my_window, text="Option 1", variable=switch, value=0, command=show_switch)
my_radio_button1.pack()
my_radio_button2 = tk.Radiobutton(my_window, text="Option 2", variable=switch, value=1, command=show_switch)
my_radio_button2.pack()

my_window.mainloop()

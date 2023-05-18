"""
1 Non-clickable category
2 No command
3 Label: textvariable. No methods
4 Message: like Label + auto-fit
5 Frame:
    5.1 container with its own coordinate
    5.2 it can contain other frames as well
    5.3 Properties: takefocus
    5.4 pack_propagate(0) to keep the size of the frame
6 LabelFrame:
    6.1 Like Frame
    6.2 title
    6.3 border
    6.4 labelanchor
7 Entry:
    7.1 Attributes: show will show its value
    7.2 Methods: get, set, delete, insert
8 Text
9 Menu
"""
import tkinter as tk


def add_a_plus():
    my_text_variable.set(my_text_variable.get() + "+")


my_window = tk.Tk()

my_frame = tk.Frame(my_window, bg="lightgreen", width=300, height=200)
my_frame.pack_propagate(0)
my_frame.pack()
frame_1 = tk.Frame(my_window, width=200, height=100, bg='white')
frame_2 = tk.Frame(my_window, width=200, height=100, bg='yellow')
frame_1.pack()
frame_2.pack()

my_label_frame = tk.LabelFrame(my_frame, labelanchor='se', text="my label frame", width=150, height=100, bg='green')
my_label_frame.pack_propagate(0)
my_label_frame.pack()

my_entry_text = tk.StringVar()
my_entry = tk.Entry(my_label_frame, textvariable=my_entry_text)
my_entry_text.set("Hello world. Is everything ok? We can work on it!!")
my_entry.pack()

my_text = tk.Text(my_label_frame)
my_text.pack()

my_text_variable = tk.StringVar()
my_text_variable.set("Hello!")
my_label = tk.Label(my_frame, textvariable=my_text_variable, width=20)
my_label.pack()

my_button = tk.Button(my_frame, text="Add a +", command=add_a_plus)
my_button.pack()

my_message = tk.Message(my_frame, textvariable=my_text_variable)
my_message.pack()

my_window.mainloop()

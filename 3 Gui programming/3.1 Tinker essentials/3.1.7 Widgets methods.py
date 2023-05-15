"""
1 Methods:
    1.1 Widget.after(time_ms, function)
    1.2 Widget.after_cancel(id)
2 widget.destroy()
"""

import tkinter as tk
TIMER = 100
TIMES = 0
MAX = 20
def timer():
    global TIMES
    TIMES +=1
    print("timer:", TIMES)
    id = my_button.after(TIMER, timer)
    if TIMES > MAX:
        my_button.after_cancel(id)
        my_frame.destroy()
def focus():
    print (my_window.focus_get())
    my_button1.focus_set()

my_window = tk.Tk()
my_button = tk.Button(my_window, text="OK", command=focus)
my_button.pack()
my_button.after(TIMER, timer)

my_frame = tk.Frame(my_window, width=100, height=100)
my_frame.pack()
my_new_label = tk.Label(my_frame, text="My new label")
my_new_label.pack()
my_new_button = tk.Button(my_frame, text="My new button")
my_new_button.pack()

my_button1 = tk.Button(my_window, text="CANCEL")
my_button1.pack()

my_window.mainloop()
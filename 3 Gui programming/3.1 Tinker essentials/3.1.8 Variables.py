"""
1 Variable:
    1.1 Observable
    1.2 Object of container class
    1.3 Explicitly created and initialized
    1.4 Typed
    1.5 To be created after the main window initialization
2 Types:
    2.1 BooleanVar
    2.2 DoubleVar
    2.3 IntVar
    2.4 StringVar
3 Default:
    3.1 integer o for IntVar;
    3.2 float 0.0 for DoubleVar;
    3.3 Boolean False for BooleanVar;
    3.4 string "" for StringVar.
4 Use:
    4.1 Constructor()
    4.2 set(VALUE)
    4.3 get()
5 Observers:
    1 Callback
    2 obsid = variable.trace(trace_mode, observer)
        2.1 trace_mode = being aware of:
            2.1.1 "r" get()
            2.1.2 "r" set()
            2.1.3 "u" del()
        2.2 observer = function
        2.3 obsid = identifier
    3 observer parameters:
        3.1 id, internal use
        3.2 ix, internal use (empty string)
        3.3 act, reason ("r", "w", "u")

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
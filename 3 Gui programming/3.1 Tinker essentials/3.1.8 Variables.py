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
    2 obsid = variable.trace(trace_mode, observer) to start tracing
        2.1 trace_mode = being aware of:
            2.1.1 "r" get()
            2.1.2 "w" set()
            2.1.3 "u" del()
        2.2 observer = function
        2.3 obsid = identifier
    3 observer parameters:
        3.1 id, internal use
        3.2 idx, internal use (empty string)
        3.3 act, reason ("r", "w", "u")
        3.4 def obs(*) if we do not need parameters
    4 variable.trace_vdelete(trace_mode,obsid) to stop tracing

"""
import tkinter as tk


def show_status():
    pass
    # print(status.get())


def swap_status():
    status.set(1 - status.get())
    # print(status.get())


def callback(id, idx, act):
    print("Status of the variable changed because of", act, id, idx)


def stopobserving():
    status.trace_vdelete("w", trace_id)


my_window = tk.Tk()
status = tk.IntVar()
my_checkbutton = tk.Checkbutton(my_window, text="value", variable=status, command=show_status)
my_checkbutton.pack()
my_button = tk.Button(my_window, text="swap status", command=swap_status)
my_button.pack()
my_button1 = tk.Button(my_window, text="stop observing", command=stopobserving)
my_button1.pack()

trace_id = status.trace("w", callback)

my_window.mainloop()

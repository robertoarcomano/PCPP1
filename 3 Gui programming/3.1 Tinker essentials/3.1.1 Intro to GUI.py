"""
1 Components:
    1.1 Title bar
    1.2 Closing button
    1.3 Icon
    1.4 Label
    1.5 Buttons
    1.6 Focus
2 Event Driven Paradigm
3 A GUI adapter is needed: Tk
4 TkInter is the Python version of Tk
5 Using Tk:
    5.1 Importing the needed tkinter components;
    5.2 Creating an application’s main window;
    5.3 Adding a set of necessary widgets to the window;
    5.4 Launching the event controller.
6 Handler = callback
7
"""
import tkinter as tk
from tkinter import messagebox


def my_click_handler():
    ask = messagebox.askquestion("Confirm", "Are you sure?") # Modal prompt
    if ask == "yes":
        window.destroy()


window = tk.Tk() # Create the window
window.title("My window") # Set a title
button = tk.Button(window, text="OK", command=my_click_handler)  # Create the button
button.place(x=10, y=10) # Assign a location to the button to make it visible
window.mainloop() # Start the mainloop (event controller)


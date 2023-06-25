import tkinter as tk
from tkinter import messagebox


def config_destroy():
    my_question = messagebox.askquestion("Confirm", "Are you sure?")
    if my_question == messagebox.YES:
        my_window.destroy()


my_window = tk.Tk()
my_window.title("My TK Window")
my_window.geometry("1024x768")

my_button = tk.Button(my_window, text="Close App", command=config_destroy)
my_button.place(x=500, y=300)

my_window.mainloop()

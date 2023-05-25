"""

"""
"""
1 Main window is shared between the user and the operating system
    1.1 window.title()
    1.2 Image
        1.2.1 prepare an icon as a PNG image;
        1.2.2 put the image in the same directory where the application resides;
        1.2.3 use a PhotoImage class constructor to convert the PNG file
              into an internal tkinter representation
              (PhotoImage() is a part of tkinter, and we’re going to tell you more about it soon)
    1.3 geometry("1024x768")
    1.4 minsize(width=640, height=480)
    1.5 maxsize(width=800, height=600)
    1.6 resizable(width=False, height=False)
    1.7 manage the closing button: protocol("WM_DELETE_WINDOW", lambda: my_window.destroy())
2 Messagebox
    2.1 askyesno
    2.2 askokcancel
    2.3
"""
import tkinter as tk
from tkinter import messagebox

my_window = tk.Tk()

my_window.title("My title")
my_window.geometry("1024x768")
my_window.tk.call('wm', 'iconphoto', my_window._w, tk.PhotoImage(file='tkinter-tutorial.png'))
my_window.minsize(width=640, height=480)
my_window.maxsize(width=800, height=600)
my_window.resizable(width=False, height=False)
my_window.protocol("WM_DELETE_WINDOW", lambda: my_window.destroy())
print(messagebox.askyesno("Are you sure?", "Well, you should tell me whether you are sure to do it.",
                          icon=messagebox.WARNING))
print(messagebox.askokcancel("OK cancel?", "Well, you should tell me whether you are sure to do Ok/Cancel."))
print(messagebox.askretrycancel("Retry cancel?", "Well, you should tell me whether you are sure to do Retry/Cancel."))
print(messagebox.askquestion("Question?", "Well, I am asking you this question..."))
print(messagebox.showinfo("Info", "This is an info!"))
print(messagebox.showerror("Error", "This is an error!"))
print(messagebox.showwarning("Warning", "This is an warning!"))

my_window.mainloop()

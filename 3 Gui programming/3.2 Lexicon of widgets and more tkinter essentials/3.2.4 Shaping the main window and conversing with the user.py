"""
1 Main window is shared between the user and the operating system
    1.1 window.title()
    1.2 Image
        1.2.1 prepare an icon as a PNG image;
        1.2.2 put the image in the same directory where the application resides;
        1.2.3 use a PhotoImage class constructor to convert the PNG file
              into an internal tkinter representation
              (PhotoImage() is a part of tkinter, and we’re going to tell you more about it soon)
"""
import tkinter as tk
my_window = tk.Tk()

my_window.title("My title")


my_window.mainloop()

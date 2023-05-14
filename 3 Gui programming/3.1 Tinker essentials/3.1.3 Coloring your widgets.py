"""
1 Normal colors (bg="", fg="")
2 Active colors (activebackground="", activeforeground="")
3 List of colors: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
4 RGB: like webpages: #0000FF
"""
import tkinter as tk


my_window = tk.Tk()
my_button = tk.Button(my_window, text="ok", bg="blue", fg="white", activebackground="#FF0000", activeforeground="#000000")
my_button.pack()
my_window.mainloop()

"""
1 Entry:
    7.1 Attributes: show will show its value
    7.2 Methods: get, set, delete, insert
2 Text
3 Menu:
    3.1 Create menu
    3.2 add_command to add a link
    3.3 add_cascade to add another menu
    3.4 underline=0 to manage hot-keys
    3.5 tearoff=0 to remove the dashed line
    3.6 accelerat and bind_all for general ALT-K binding
    3.7 entryconfigure((i, prop=value) instead of config()
"""
import tkinter as tk
from tkinter import messagebox

def about():
    print("about")


def quit():
    if tk.messagebox.askyesno("app", "Are you sure"):
        my_window.destroy()


def enable_export():
    file_menu.entryconfigure(3, state=tk.ACTIVE)

my_window = tk.Tk()

my_menu = tk.Menu(my_window)
file_menu = tk.Menu(my_menu, tearoff=0)
menu_open_recent = tk.Menu(file_menu, tearoff=0)
menu_open_recent.add_command(label="file1...")
menu_open_recent.add_command(label="file2...")
file_menu.add_command(label="Open", command=lambda: print("Open"), underline=0)
file_menu.add_cascade(label="Open recent...", menu=menu_open_recent)
file_menu.add_command(label="Save", underline=0, accelerator="Alt-S", command=lambda: print("Save"))
file_menu.add_command(label="Export", underline=0, accelerator="Alt-E", command=lambda: print("Export"), state=tk.DISABLED)
file_menu.add_command(label="Enable export", underline=0, command=enable_export)
my_window.bind_all("<Alt-s>", lambda x: print("save"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, underline=0)
my_menu.add_cascade(label="File", menu=file_menu, underline=0)
my_menu.add_command(label="About", command=about, underline=0)

my_window.config(menu=my_menu)

my_window.mainloop()

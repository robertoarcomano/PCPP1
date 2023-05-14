"""
1 Geometry managers:
    1.1 Place (x, y, width, height)
    1.2 Pack (side, fill)
    1.3 Grid (row, column, rowspan, columnspan)
"""
import tkinter as tk

my_window = tk.Tk()
my_window.geometry("1024x768")
my_buttons = []
SHIFT = 40
COLUMN_START=200
for i in range(0,3):
    my_buttons.append(tk.Button(my_window, text="ok " + str(i)))
    my_buttons[i].place(x=(i+1)*SHIFT+COLUMN_START, y=(i+1)*SHIFT)
for i in range(3, 6):
    my_buttons.append(tk.Button(my_window, text="ok " + str(i)))
    my_buttons[i].place(x=(i + 1) * SHIFT+COLUMN_START, y=(i + 1) * SHIFT, width=SHIFT*2*(i-2), height=i*10)
for i in range(6, 9):
    my_buttons.append(tk.Button(my_window, text="ok " + str(i)))
    my_buttons[i].grid(row=i, column=i)

my_buttons1 = []
my_window1 = tk.Tk()
for i in range(0, 3):
    my_buttons1.append(tk.Button(my_window1, text="ok " + str(i)))
    my_buttons1[i].pack(side=tk.RIGHT)

my_buttons2 = []
my_window2 = tk.Tk()
for i in range(0, 3):
    my_buttons2.append(tk.Button(my_window2, text="ok " + str(i)))
    my_buttons2[i].pack(side=tk.BOTTOM)

my_buttons3 = []
my_window3 = tk.Tk()
my_buttons3.append(tk.Button(my_window3, text="ok " + str(0)))
my_buttons3.append(tk.Button(my_window3, text="ok " + str(1)))
my_buttons3.append(tk.Button(my_window3, text="ok " + str(2)))
my_buttons3[0].pack(side=tk.RIGHT, fill=tk.Y)
my_buttons3[1].pack()
my_buttons3[2].pack()

my_window3.mainloop()

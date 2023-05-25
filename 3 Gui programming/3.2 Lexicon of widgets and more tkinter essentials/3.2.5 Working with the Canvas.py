"""
1 Create canvas: tk.Canvas()
2 create_line
    2.1 create_line(x0,y0,x1,y1)
    2.2 multiple lines using create_line
    2.3 options: arrow, fill (color), smooth (rounded), width
3 create_rectangle(x0,y0,x1,y1)
    3.1 options outline, fill, width
4 polygon similar to lines but without the last line
5 oval: inscribed inside a rectangle
6 arc: inscribed inside a rectangle
    6.1 style: pieslice, chord, arc
    6.2 start (angle)
    6.3 extent
7 text
8 image
    8.1 JPEG using PIL package for the conversion
"""
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk
my_window = tk.Tk()
my_window.geometry("640x480")

my_canvas = tk.Canvas(width=640, height=480, bg="lightgreen")
my_canvas.create_line(1, 1, 640, 480)
my_canvas.create_rectangle(2, 2, 637, 477, outline="red", width=5)
my_canvas.create_rectangle(300, 220, 340, 260, fill="orange")
my_canvas.create_polygon(340, 260, 360, 260, 360, 280, outline="blue", width=2, fill="yellow")
my_canvas.create_line(320, 1, 320, 240, 1, 240, arrow=tk.BOTH, fill="blue", smooth=True, width=2)
my_canvas.create_oval(260, 260, 340, 300, fill="green", outline="green", width=2)

my_canvas.create_arc(260, 260, 340, 300, fill="black", outline="black", width=2,
                     style=tk.PIESLICE, start=0, extent=90)
my_canvas.create_arc(260, 260, 340, 300, fill="black", outline="black", width=2,
                     style=tk.ARC, start=90, extent=90)
my_canvas.create_arc(260, 260, 340, 300, fill="black", outline="black", width=2,
                     style=tk.CHORD, start=180, extent=90)
my_canvas.create_text(320, 320, text="ok, good!", fill="blue", width=40, justify=tk.LEFT)
my_canvas.create_rectangle(300, 305, 340, 335)

image = tk.PhotoImage(file='tkinter-tutorial.png')
my_canvas.create_image(480, 120, image=image)

jpg = PIL.Image.open('tkinter-tutorial.jpg')
image1 = PIL.ImageTk.PhotoImage(jpg)
my_canvas.create_image(160, 360, image=image1)

my_canvas.grid(row=0)
my_canvas.pack()

my_window.mainloop()

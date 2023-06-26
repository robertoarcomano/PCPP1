import tkinter as tk
from tkinter import messagebox


def config_destroy():
    my_question = messagebox.askquestion("Confirm", "Are you sure?")
    if my_question == messagebox.YES:
        my_window.destroy()


my_window = tk.Tk()
my_window.title("My TK Window")
my_window.geometry("1024x750")

my_frame1 = tk.Frame(my_window, width=1024, height=250, background="green")
my_frame1.pack()
my_frame2 = tk.Frame(my_window, width=1024, height=250, background="pink")
my_frame2.pack()
my_frame3 = tk.Frame(my_window, width=1024, height=250, background="brown")
my_frame3.pack()
my_frame4 = tk.Frame(my_window, width=1024, height=50, background="lightblue")

my_button = tk.Button(my_frame1, text="Close App", command=config_destroy,
                      activebackground="green", activeforeground="white")

my_button.place(x=450, y=120)

text_var = tk.StringVar()
radio_var = tk.IntVar()
my_radiobutton1 = tk.Radiobutton(my_frame2, text="Radio1", variable=radio_var, value=1)
my_radiobutton1.pack(side=tk.LEFT, fill=tk.Y)

my_radiobutton2 = tk.Radiobutton(my_frame2, text="Radio2", variable=radio_var, value=2)
my_radiobutton2.pack(side=tk.LEFT, fill=tk.Y)

my_label = tk.Label(my_frame4, textvariable=radio_var)
my_label.pack()
my_frame4.pack()

my_checkbutton1 = tk.Checkbutton(my_frame3, text="Check 1", command=lambda: messagebox.showinfo("Check 1", "Check 1"))
my_checkbutton1.grid(row=1, column=1, pady=51, padx=400)
my_checkbutton2 = tk.Checkbutton(my_frame3, text="Check 2",
                                 command=lambda: messagebox.showwarning(text_var.get(), text_var.get()))
my_checkbutton2.grid(row=2, column=1, pady=51, padx=400)

my_entry = tk.Entry(my_frame2, textvariable=text_var)
my_entry.pack()
my_window.mainloop()

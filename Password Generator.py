import random
import tkinter as tk
from tkinter import *

global value_error, pass_notice
allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789/?.,!@#$%^&*()-_=+[]{}|"


def enter():
    try:
        num_of_digits = int(e.get())
        if num_of_digits > 0:
            res = generate_password(num_of_digits)
            result = Label(root, text=("Your password is " + res))
            result.pack()
        else:
            value_error()
    except ValueError:
        value_error()


def value_error():
    val_error = Label(root, text="Please enter a POSITIVE NUMBER")
    val_error.pack()


def generate_password(num_of_digits):
    res = ""
    for i in range(num_of_digits):
        res = res + random.choice(allowed)
    return res


root = tk.Tk()
title = Label(root, text="Password Generator")
title.pack()

e = Entry(root, width=50)
e.pack()

enter_button = Button(root, text="ENTER", padx=10, command=enter)
enter_button.pack()

root.mainloop()

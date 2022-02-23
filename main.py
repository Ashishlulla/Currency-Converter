import tkinter as tk
from tkinter import ttk
from tkinter import *

win = tk.Tk()
win.title("Currency Converter")
win.geometry("590x350")
win.resizable(0,0)
win.config(bg="#E8E8E8")


# -------------------- Labels ----------------------------

from_label = tk.Label(win,text="From:", fg="#80322E", font="Arial 12 bold", bg="#E8E8E8")
from_label.place(x=75, y =50)

to_label = tk.Label(win,text="To:", fg="#80322E", font="Arial 12 bold", bg="#E8E8E8")
to_label.place(x=350, y =50)

amount_label = tk.Label(win , text="Enter the Amount to Convert :",font="Arial 12 bold",bg="#E8E8E8")
amount_label.place(x=100, y=120)

total_label = tk.Label(win , text="Total Converted Amount :", font="Arial 12 bold", bg="#E8E8E8")
total_label.place(x=100, y=200)

project_label = tk.Label(win , text="Developed by Ashish Rajesh Lulla", fg="#80322E", bg="#E8E8E8")
project_label.place(x=180, y=320)

# ---------------------- Entry Boxes -------------------------

amount_var = StringVar()
amount_entry = ttk.Entry(win, width=63, textvariable=amount_var)
amount_entry.place(x=100, y=160)

total_var = StringVar()
total_entry = ttk.Entry(win, width=63, textvariable=total_var)
total_entry.place(x=100, y=240)


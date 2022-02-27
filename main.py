import tkinter as tk
from tkinter import ttk
from tkinter import *

win = tk.Tk()
win.title("Currency Converter")
win.geometry("590x350")
win.resizable(0,0)
win.config(bg="#E8E8E8")

# ------------------------------- Functionality -------------------------

def convert():
    amount = float(amount_var.get())
    currency1 = from_var.get()
    currency2 = to_var.get()
    print(amount, currency1, currency2)

    if currency1 == "Afghani":
        if currency2 == "Canadian Dollar":
            total = amount*0.014
            total_var.set(total)
        elif currency2 == "Chinese Yuan":
            total = amount*0.069
            total_var.set(total)
        elif currency2 == "Euro":
            total = amount*0.0096
            total_var.set(total)
        elif currency2 == "Indian Rupee":
            total = amount*0.81
            total_var.set(total)
        elif currency2 == "Israeli New Shekel":
            total = amount*0.035
            total_var.set(total)
        elif currency2 == "Kuwaiti Dinar":
            total = amount*0.0033
            total_var.set(total)
        elif currency2 == "Pakistani rupee":
            total = amount*1.92
            total_var.set(total)
        elif currency2 =="Russian Rubble":
            total = amount*0.86
            total_var.set(total)
        elif currency2 == "US Dollar":
            total = amount*0.011
            total_var.set(total)
    elif currency1 == "Canadian Dollar":
        if currency2 == "Afghani":
            total = amount*72.44
            total_var.set(total)
        elif currency2 == "Chinese Yuan":
            total = amount*4.97
            total_var.set(total)
        elif currency2 == "Euro":
            total = amount*0.69
            total_var.set(total)
        elif currency2 == "Indian Rupee":
            total = amount*58.69
            total_var.set(total)
        elif currency2 == "Israeli New Shekel":
            total = amount*2.53
            total_var.set(total)
        elif currency2 == "Kuwaiti Dinar":
            total = amount*0.24
            total_var.set(total)
        elif currency2 == "Pakistani rupee":
            total = amount*139.06
            total_var.set(total)
        elif currency2 =="Russian Rubble":
            total = amount*61.86
            total_var.set(total)
        elif currency2 == "US Dollar":
            total = amount*0.79
            total_var.set(total)
    elif currency1 == "Chinese Yuan":
        if currency2 == "Afghani":
            total = amount*14.57
            total_var.set(total)
        elif currency2 == "Canadian Dollar":
            total = amount*0.20
            total_var.set(total)
        elif currency2 == "Euro":
            total = amount*0.14
            total_var.set(total)
        elif currency2 == "Indian Rupee":
            total = amount*11.80
            total_var.set(total)
        elif currency2 == "Israeli New Shekel":
            total = amount*0.51
            total_var.set(total)
        elif currency2 == "Kuwaiti Dinar":
            total = amount*0.048
            total_var.set(total)
        elif currency2 == "Pakistani rupee":
            total = amount*27.97
            total_var.set(total)
        elif currency2 =="Russian Rubble":
            total = amount*12.50
            total_var.set(total)
        elif currency2 == "US Dollar":
            total = amount*0.16
            total_var.set(total)

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


# -------------------- Combo Boxes----------------------------

from_var = StringVar()
from_comb = ttk.Combobox(win, width=25, textvariable=from_var)
from_comb['values'] = ("Afghani","Canadian Dollar","Chinese Yuan","Euro","Indian Rupee","Israeli New Shekel","Kuwaiti Dinar","Pakistani rupee","Russian Rubble","US Dollar")
from_comb.current(4)
from_comb.place(x=75, y=80)

to_var = StringVar()
to_comb = ttk.Combobox(win, width=25, textvariable=to_var)
to_comb["values"] = ("Afghani","Canadian Dollar","Chinese Yuan","Euro","Indian Rupee","Israeli New Shekel","Kuwaiti Dinar","Pakistani rupee","Russian Rubble","US Dollar")
to_comb.current(9)
to_comb.place(x=350, y=80)


# --------------------- Buttons ------------------------------

convert_button = tk.Button(win, text="Convert", width=18,font="Arial 12 bold", border=0, bg="red", fg="white", command=convert)
convert_button.place(x=100,y=280)

exit_button = tk.Button(win, text="Quit", width=18,font="Arial 12 bold", border=0, bg="red", fg="white", command=quit)
exit_button.place(x=300, y=280)


win.mainloop()


import tkinter as tk
from tkinter import *


HEIGHT = 400
WIDTH = 800

root = tk.Tk()
root.title("Currency Converter")
root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def convert(left, right, clicked, clicked1):
    d = clicked.get()
    d1 = clicked1.get()

    l = left.get()
    l = float(l)

    if d == "United States Dollar":
        if d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.86)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 114.38)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.73)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.35)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.24)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.92)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 6.44)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 7.78)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.42)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 81.5)

    elif d == "Euro":
        if d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.16)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 132.54)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.84)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.56)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.44)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 1.07)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 7.47)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 9.02)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.64)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 88.1)

    elif d == "Pound Sterling":
        if d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.37)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 1.19)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 157.22)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.85)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.70)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 1.27)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 8.85)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 10.69)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.94)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 100.27)

    elif d == "Japanese Yen":
        if d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.0088)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.0075)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.0064)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.012)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.011)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.0081)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 0.056)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.068)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.012)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 0.62)

    elif d == "Australian Dollar":
        if d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.74)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.64)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.54)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 84.71)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.92)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.68)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 4.77)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 5.77)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.05)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 56.64)

    elif d == "Canadian Dollar":
        if d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.81)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.70)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.59)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.09)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 92.34)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.75)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 5.20)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 6.29)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.14)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 61.23)

    elif d == "Swiss Franc":
        if d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.08)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.93)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.79)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.46)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.34)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 123.22)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 6.97)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 8.42)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.53)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 89.39)

    elif d == "Chinese Yuan":
        if d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.16)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.13)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.11)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.21)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.19)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.14)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 17.77)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 1.21)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.22)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 12.03)

    elif d == "Hong Kong Dollar":
        if d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.13)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.11)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.094)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.17)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.16)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.12)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 0.83)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 14.71)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.18)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 10.56)

    elif d == "New Zeland Dollar":
        if d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.71)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.61)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.51)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.95)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.87)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.65)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 4.54)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 5.49)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 80.73)
        elif d1 == "INR":
            right.delete(0, END)
            right.insert(0, l * 51.5)

    elif d == "INR":
        if d1 == "INR":
            right.delete(0, END)
            right.insert(0, l)
        elif d1 == "United States Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.012)
        elif d1 == "Euro":
            right.delete(0, END)
            right.insert(0, l * 0.011)
        elif d1 == "Pound Sterling":
            right.delete(0, END)
            right.insert(0, l * 0.0100)
        elif d1 == "Australian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.018)
        elif d1 == "Canadian Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.016)
        elif d1 == "Swiss Franc":
            right.delete(0, END)
            right.insert(0, l * 0.011)
        elif d1 == "Chinese Yuan":
            right.delete(0, END)
            right.insert(0, l * 0.083)
        elif d1 == "Hong Kong Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.095)
        elif d1 == "Japanese Yen":
            right.delete(0, END)
            right.insert(0, l * 1.62)
        elif d1 == "New Zeland Dollar":
            right.delete(0, END)
            right.insert(0, l * 0.019)

entryframe = tk.Frame(root, bg='lightblue')
entryframe.place(relwidth=1, relheight=1)

text = tk.Label(entryframe, text="Offline Currency Converter", font=1, bg="lightblue")
text.place(relx=0.38, rely=0.15)

left = tk.Entry(entryframe, font=1, bg='white')
left.place(relx=0.1, rely=0.35, relheight=0.05, relwidth=0.2)

right = tk.Entry(entryframe, font=1, bg='white')
right.place(relx=0.7, rely=0.35, relheight=0.05, relwidth=0.2)

options = ["United States Dollar","INR","Euro","Japanese Yen","Pound Sterling","Australian Dollar","Canadian Dollar","Swiss Franc","Chinese Yuan","Hong Kong Dollar","New Zeland Dollar"]

clicked = StringVar()

clicked.set("INR")

drop = OptionMenu(root, clicked, *options)
drop.place(relx=0.1, rely=0.45, relheight=0.05, relwidth=0.2)

options1 = ["United States Dollar","INR","Euro","Japanese Yen","Pound Sterling","Australian Dollar","Canadian Dollar","Swiss Franc","Chinese Yuan","Hong Kong Dollar","New Zeland Dollar"]

clicked1 = StringVar()

clicked1.set("INR")

drop1 = OptionMenu(root, clicked1, *options1)
drop1.place(relx=0.7, rely=0.45, relheight=0.05, relwidth=0.2)

button = tk.Button(entryframe, text="Convert", font=1, command=lambda: convert(left, right, clicked, clicked1))
button.place(relx=0.4, rely=0.5, relheight=0.1, relwidth=0.2)
root.mainloop()

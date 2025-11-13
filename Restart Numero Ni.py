from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Testing")

#-----TESTING ONE-----
def calculate_celsius(*args):
    try:
        c = float(celsius.get())
        f = (c * 9/5) + 32
        far.set(f)
    except ValueError:
        pass

#-----TESTING TWO-----
def calculate_weight(*args):
    try:
        kg = float(kilograms.get())
        p = (kg * 2.2)
        far.set(p)
    except ValueError:
        pass
    

#-----LAYOUT-----
mainframe = ttk.Frame(root, padding=(40, 30, 40, 30))
mainframe.grid(column = 1, row = 1, sticky = (N, W, E, S))

#-----TESTING ONE-----
ttk.Label(mainframe, text="Celsius to Fahrenheit").grid(column=0, row=0, columnspan=2)
celsius = StringVar()
far = StringVar()
ttk.Entry(mainframe, width=10, textvariable=celsius).grid(column=0, row=1)
ttk.Button(mainframe, text="Convert", command=calculate_celsius).grid(column=1, row=1)
ttk.Label(mainframe, textvariable=far).grid(column=0, row=2, columnspan=2)

#-----TESTING TWO-----
ttk.Label(mainframe, text="Kilograms to Pounds").grid(column=0, row=5, columnspan=2)
kilograms = StringVar()
far = StringVar()
ttk.Entry(mainframe, width=10, textvariable=celsius).grid(column=0, row=6)
ttk.Button(mainframe, text="Convert", command=calculate_weight).grid(column=1, row=6)
ttk.Label(mainframe, textvariable=far).grid(column=0, row=7, columnspan=2)

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        c = float(celsius.get())
        f = (c * 9/5) + 32
        far.set(f)
    except ValueError:
        pass

def calculate(*args):
    try:
        c = float(celsius.get())
        f = (c * 9/5) + 32
        far.set(f)
    except ValueError:
        pass

root = Tk()
root.title("Temperature Converter")

mainframe = ttk.Frame(root, padding=(40, 30, 40, 30))
mainframe.grid(column = 1, row = 1, sticky = (N, W, E, S))


celsius = StringVar()
celsuis_entry = ttk.Entry(mainframe, width = 7, textvariable = celsius)
celsuis_entry.grid(column = 1, row = 1, sticky = (W, E))

far = StringVar()
ttk.Label(mainframe, textvariable=far).grid(column=2, row=2, sticky=(N, S))

far = StringVar()
far_Label = ttk.Label(mainframe, textvariable=far)
far_Label.grid(column=1, row=2, sticky=(W,))

calc_button = ttk.Button(mainframe, text="Cake it", command=calculate)
calc_button.grid(column=1, row=3, sticky=(S, W))

ttk.Label(mainframe, text="C").grid(column=2, row=1, sticky=(W,))
ttk.Label(mainframe, text="=").grid(column=0, row=2, sticky=(E,))
ttk.Label(mainframe, text="F").grid(column=2, row=2, sticky=(S,))

root.mainloop()
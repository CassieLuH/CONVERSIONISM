from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Multi Converter")

# ===== Temperature Converter =====
def convert_temp():
    try:
        c = float(celsius.get())
        f = (c * 9/5) + 32
        far.set(f"{f:.2f}")
    except ValueError:
        far.set("Invalid")

# ===== Length Converter =====
def convert_length():
    try:
        m = float(meters.get())
        ft = m * 3.28084
        feet.set(f"{ft:.2f}")
    except ValueError:
        feet.set("Invalid")

# ===== Weight Converter =====
def convert_weight():
    try:
        kg = float(kilograms.get())
        lbs = kg * 2.20462
        pounds.set(f"{lbs:.2f}")
    except ValueError:
        pounds.set("Invalid")

# ===== Layout =====
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Temperature
ttk.Label(mainframe, text="Celsius to Fahrenheit").grid(column=0, row=0, columnspan=2)
celsius = StringVar()
far = StringVar()
ttk.Entry(mainframe, width=10, textvariable=celsius).grid(column=0, row=1)
ttk.Button(mainframe, text="Convert", command=convert_temp).grid(column=1, row=1)
ttk.Label(mainframe, textvariable=far).grid(column=0, row=2, columnspan=2)

# Length
ttk.Label(mainframe, text="Meters to Feet").grid(column=0, row=3, columnspan=2)
meters = StringVar()
feet = StringVar()
ttk.Entry(mainframe, width=10, textvariable=meters).grid(column=0, row=4)
ttk.Button(mainframe, text="Convert", command=convert_length).grid(column=1, row=4)
ttk.Label(mainframe, textvariable=feet).grid(column=0, row=5, columnspan=2)

# Weight
ttk.Label(mainframe, text="Kilograms to Pounds").grid(column=0, row=6, columnspan=2)
kilograms = StringVar()
pounds = StringVar()
ttk.Entry(mainframe, width=10, textvariable=kilograms).grid(column=0, row=7)
ttk.Button(mainframe, text="Convert", command=convert_weight).grid(column=1, row=7)
ttk.Label(mainframe, textvariable=pounds).grid(column=0, row=8, columnspan=2)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
import tkinter as tk

root = tk.Tk()

# Create a DoubleVar instance
my_var = tk.DoubleVar()

# Set an initial value
my_var.set(3.14)

# Create a label and associate it with the DoubleVar
my_label = tk.Label(root, textvariable=my_var)
my_label.pack()

root.mainloop()

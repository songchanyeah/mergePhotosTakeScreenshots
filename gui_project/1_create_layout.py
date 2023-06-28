from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

# File Frame (Add file, select and delete)
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add a File")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Select and Delete")
btn_del_file.pack(side="right")

# List Frame
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Save Path Frame
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=5)

btn_dest_path = Button(path_frame, text="Find", width=10)
btn_dest_path.pack(side="right")

# Option Frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. Width option
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Keep Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=12)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. Space option
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["None", "Narrow", "Normal", "Wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=12)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

#3. File format option
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=12)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress Bar
frame_progress = LabelFrame(root, text="Progress Status")
frame_progress.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5, ipady=5)

# Execute Frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right")

root.resizable(False, False)
root.mainloop()
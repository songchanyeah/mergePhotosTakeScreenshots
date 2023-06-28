import tkinter.ttk as ttk  
import tkinter.messagebox as msgbox
from tkinter import * # __all__ 
from tkinter import filedialog # submodule

root = Tk()
root.title("Nado GUI")

# Add File
def add_file():
    files = filedialog.askopenfilenames(title="Select an Image File", \
                                        filetypes=(("PNG", "*.png"), ("Any", "*.*")), \
                                        initialdir="C:/")

    # List of Files Users Selected
    for file in files:
        list_file.insert(END, file)

# Select and Delete File
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# Save Path (Folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == None:
        return
    # print(folder_selected)
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)

def start():
    print("Width: ", cmb_width.get())
    print("Space: ", cmb_space.get())
    print("Format: ", cmb_format.get())

    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add Image Files")
        return
    
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning," "Select Save Path")
        return
    

# File Frame (Add file, select and delete)
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add a File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Select and Delete", command=del_file)
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
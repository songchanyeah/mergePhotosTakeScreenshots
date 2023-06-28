import os
import tkinter.ttk as ttk  
import tkinter.messagebox as msgbox
from tkinter import * # __all__ 
from tkinter import filedialog # submodule
from PIL import Image

root = Tk()
root.title("Nado GUI")

# Add File
def add_file():
    files = filedialog.askopenfilenames(title="Select an Image File", \
                                        filetypes=(("PNG", "*.png"), ("Any", "*.*")), \
                                        initialdir=r"C:\Users\cyhso\Desktop\Nadocoding")

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
    if folder_selected == '':
        return
    # print(folder_selected)
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)

# Merge Images
def merge_image():
    # print("Width: ", cmb_width.get())
    # print("Space: ", cmb_space.get())
    # print("Format: ", cmb_format.get())

    try:
        # width
        img_width = cmb_width.get()
        if img_width =="Keep Original":
            img_width = -1 # when -1, keep oroginal
        else:
            img_width = int(img_width)

        # Space
        img_space = cmb_space.get()
        if img_space == "Narrow":
            img_space = 30
        elif img_space == "Normal":
            img_space = 60
        elif img_space == "Wide":
            img_space = 90
        else:
            img_space = 0

        # Format
        img_format = cmb_format.get().lower() # get PNG, JPG, BMP and change them to lower case

        ###############################################

        images = [Image.open(x) for x in list_file.get(0, END)]

        image_sizes = [] # [(width1, height1), (width2, height2), ...]
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]
        


        images = [Image.open(x) for x in list_file.get(0, END)]
        widths, heights = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(heights)

        # prepare a sketchbook
        if img_space > 0:
            total_height += (img_space * (len(images) -1))
            if img_width > -1:
                img = img.resize(image_sizes[idx])

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # white  background
        y_offset += (img.size[1] + img_space) # y location
        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1] # height

        for idx, img in enumerate(images):
            result_img.paste(img, (0, y_offset))
            y_offset += img.size[1]

            progress = (idx + 1) / len(images) * 100 # calculating percentage information 
            p_var.set(progress)
            progress_bar.update()

        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Alert", "Merge has been completed.")
    except Exception as err:
        msgbox.showerror("Error: ",err)

def start():
    # print("Width: ", cmb_width.get())
    # print("Space: ", cmb_space.get())
    # print("Format: ", cmb_format.get())

    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add Image Files")
        return
    
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning," "Select Save Path")
        return
    
    merge_image()

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

btn_dest_path = Button(path_frame, text="Find", width=10, command=browse_dest_path)
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

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right")

root.resizable(False, False)
root.mainloop()
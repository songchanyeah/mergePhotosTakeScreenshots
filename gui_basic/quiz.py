from tkinter import *
import os

root = Tk()
root.title("No Title - Windows Notepad")
root.geometry("640x480")

# 열기, 저장 파일 이름
filename = " mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, 'r', encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="End", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Edit")
menu.add_cascade(label="Selection")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()

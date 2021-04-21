from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import shutil
import os

filename = ""


def browseFiles():
    global filename
    filename = filedialog.askdirectory(initialdir="/", title="Select a File")


def movefile():
    if filename == "":
        tkinter.messagebox.showerror("MC World Tool", "No Folder Selected!")
    else:
        shutil.move(filename, mcfile)
        print(mcfile)
        tkinter.messagebox.showinfo("MC World Tool", "Map Moved Successfully!")


root = Tk()
root.title("MC Map Tool")
root.geometry("250x80")
root.resizable(False, False)
p = PhotoImage(file='map.png')
root.iconphoto(False, p)

mcfile = r'C:/Users/'
mcfile = mcfile + os.getlogin()
mcfile = mcfile + r'/AppData/Roaming/.minecraft/saves/'

txt = Label(root, text="Select a Map Folder to Move.")
txt.pack(side=TOP)

fle = Button(root, text="Choose a Folder", command=browseFiles)
fle.pack(side=TOP)

btn = Button(root, text="Move Map", command=movefile)
btn.pack(side=TOP)

root.mainloop()

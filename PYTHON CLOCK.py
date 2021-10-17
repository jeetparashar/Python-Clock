from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    print(string)
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("SF Sports Night", 80), background= "black", foreground= "cyan" )
label.pack(anchor='center')
time()

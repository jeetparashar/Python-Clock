# Python-Clock
This clock is created using python programming language , It's a 12Hrs format clock. The font of this clock can be change  you just need to download the font from the given  link  you can choose any font as you like 

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

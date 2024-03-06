Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *

count = 0

def button_clicked():
    global count
    count = count + 100
    count_text.config(text=count)

window = Tk()

count_text = Label(text="0")
count_text.pack()

button = Button(text="click", command=button_clicked)
button.pack()

window.mainloop()
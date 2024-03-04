Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk

def change_color(color):
    root.configure(bg=color)

root = tk.Tk()
root.title("Color Changer")

red_button = tk.Button(root, text="Red", command=lambda: change_color("red"))
red_button.pack(side="left", padx=10)

blue_button = tk.Button(root, text="Blue", command=lambda: change_color("blue"))
blue_button.pack(side="right", padx=10)

root.mainloop()
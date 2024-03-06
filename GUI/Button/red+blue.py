import tkinter as tk

def change_color(color):
    root.configure(bg=color)

root = tk.Tk()
root.title("Color Changer")

red_button = tk.Button(root, text="Red", command=lambda: change_color("red"))
red_button.pack(side="left", padx=15)

blue_button = tk.Button(root, text="Blue", command=lambda: change_color("blue"))
blue_button.pack(side="right", padx=15)

root.mainloop()
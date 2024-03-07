from tkinter import*

class Student():

    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def display_grade(self):
        print(self.grade)

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name

def show_grade():
    grade_label.config(text=csc_level_2[0].get_grade())
    pass

def show_name():
    name_label.config(text=csc_level_2[0].get_name())
    pass

csc_level_2 = []

csc_level_2.append(Student("Kajah"))
csc_level_2[0].set_grade("Not Achieved")
csc_level_2[0].display_name()

csc_level_2.append(Student("Shauryya"))
csc_level_2[1].set_grade("Excellence")
csc_level_2[1].display_name()

csc_level_2.append(Student("Gabby"))
csc_level_2[2].set_grade("Merit")
csc_level_2[2].display_name()

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Kajah")
students_listbox.insert(0, "Shauryya")
students_listbox.insert(0, "Gabby")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

name_label = Label()
name_label.pack()

show_name_btn = Button(text="Show Name", command=show_name)
show_name_btn.pack()

window.mainloop()
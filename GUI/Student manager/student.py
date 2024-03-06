from tkinter import*

class Student():

    def __innit__(self, name):
        self.first_name = name
    
    def display_name(self):
        print(self.first_name)

    def set_grade(self, grade):
        self.grade = grade

    def display_grade(self):
        print(self.grade)

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

def show_grade():
    grade_label.config(text=csc_level_2[0].get_grade)
    pass

csc_level_2 = []

csc_level_2.append(Student("Kajah"))
csc_level_2[0].set_grade("Not Achieved")
csc_level_2[0].display_name()

csc_level_2.append(Student("Shauryya"))
csc_level_2[1].set_grade("Excellence")
csc_level_2[1].display_name()

window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
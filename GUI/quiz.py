from tkinter import*
names = []

class QuizStarter:
    def __init__(self, parent):
        
        background_color = "lightsteelblue"

        self.quiz_frame = Frame(parent, bg= background_color, padx=100, pady=100)






#Starting point#
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    #quiz_instance = QuizStarter(root) #making an instanse of the class QuizStarter#
    root.mainloop()

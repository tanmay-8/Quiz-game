
from tkinter import*
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain()):
        self.quiz_brain  = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("500x450")
        self.window.configure(bg="#375362")


        self.canva = Canvas(width=300,height=250,highlightthickness=0,border=0,bg="white")
        self.title = self.canva.create_text(150,125,text=self.quiz_brain.next_question(),font=("Courier",10,"bold"),width=280)
        self.canva.place(x=100,y=50)
        
        self.label = Label(text=f"score:{self.quiz_brain.score}",font=("",20,""),bg="#375362",fg="white")
        self.label.place(y=10,x=400)
    
        self.check = PhotoImage(file=r'.\images\true.png')
        self.cross = PhotoImage(file=r'.\images\false.png')

        self.checkbt = Button(border=0,borderwidth=0,command=self.true_pressed)
        self.checkbt.configure(image=self.check,bg="#375362")
        self.checkbt.place(x=130,y=330)

        self.crossbt = Button(border=0,borderwidth=0,command=self.false_pressed)
        self.crossbt.configure(image=self.cross,bg="#375362")
        self.crossbt.place(x=270,y=330)
        
        self.window.mainloop()

    def nextque(self):
        self.quiz_brain.generate()
        question = self.quiz_brain.next_question()
        self.canva.itemconfig(self.title,text=question)
        self.canva.configure(bg="white")
        self.checkbt.configure(state=NORMAL)
        self.crossbt.configure(state=NORMAL)
    
    def right_answer(self):
        self.canva.configure(bg="#94f2ad")
        
    def wrong_answer(self):
        self.canva.configure(bg="#f0867a")
    
    def true_pressed(self):
        ans = "true"
        if((self.quiz_brain.current_question.answer).lower()==ans):
            self.checkbt.configure(state=DISABLED)
            self.crossbt.configure(state=DISABLED)
            self.quiz_brain.score += 1
            self.label.configure(text=f"score:{self.quiz_brain.score}",font=("",20,""),bg="#375362",fg="white")
            self.right_answer()
            print("right")
        else:
            self.wrong_answer()
            print("wrong")
        
        self.quiz_brain.question_list.remove(self.quiz_brain.current_question)
        self.window.after(2000,func=self.nextque)

    def false_pressed(self):
        ans="false"
        if((self.quiz_brain.current_question.answer).lower()==ans):
            self.checkbt.configure(state=DISABLED)
            self.crossbt.configure(state=DISABLED)
            self.quiz_brain.score += 1
            self.label.configure(text=f"score:{self.quiz_brain.score}",font=("",20,""),bg="#375362",fg="white")
            self.right_answer()
            print("right")
        else:
            self.wrong_answer()
            print("wrong")
        self.quiz_brain.question_list.remove(self.quiz_brain.current_question)
        self.window.after(2000,func=self.nextque)
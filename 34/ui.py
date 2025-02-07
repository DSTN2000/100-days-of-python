from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Aria', 20, 'italic')

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0,row=1, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(150,125, width=280,text='', font=FONT, fill=THEME_COLOR)
        self.get_next_question()

        true_image,false_image = map(lambda x: PhotoImage(file=f'34/images/{x}'), ['true.png', 'false.png'])
        images = {'true': true_image, 'false': false_image}
        self.buttons = {k:v for (k,v) in zip(['true', 'false'], list(map(lambda x: Button(image=images[x],
                                                                                   command=(lambda : self.give_feedback(x))),
                                                                                   ['true','false'])))}
        self.buttons['true'].grid(column=1, row=2, pady=50)
        self.buttons['false'].grid(column=0, row=2, pady=50)



        self.window.mainloop()
    
    def get_next_question(self):
        text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=text)
    
    def give_feedback(self, x):
        is_right = self.quiz.check_answer(x)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.after = self.window.after(1000, self.update_score)
        for button in self.buttons.values():
            button.config(state='disabled')

    def update_score(self):
        for button in self.buttons.values():
            button.config(state='active')
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.get_next_question()
        else:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            text = f"You've completed the quiz" \
            f"\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=text)           
            for button in self.buttons.values():
                button.config(state='disabled')

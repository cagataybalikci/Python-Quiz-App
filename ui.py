from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(text="True", highlightthickness=0,padx=20,pady=20)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(text="False", highlightthickness=0,padx=20,pady=20)
        self.false_button.grid(row=2, column=1)
        self.window.mainloop()

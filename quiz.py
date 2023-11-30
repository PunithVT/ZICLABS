import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, question, choices, correct_choice, explanation):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice
        self.explanation = explanation

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.questions = [
            Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1, "Paris is known for its iconic Eiffel Tower."),
            Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2, "Mars gets its reddish appearance from iron oxide."),
            Question("Which famous scientist developed the theory of relativity?", ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"], 3, "Albert Einstein revolutionized our understanding of space and time."),
            Question("In which year was Python programming language first released?", ["1989", "1991", "1995", "2000"], 2, "Guido van Rossum released Python in 1991."),
            Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2, "The Blue Whale holds the title of the largest mammal."),
        ]

        self.current_question_index = 0
        self.score = 0

        self.setup_ui()

    def setup_ui(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.choice_var = tk.StringVar()

        self.choice_buttons = []

        for i in range(4):
            choice_button = tk.Radiobutton(self.master, text="", variable=self.choice_var, value="", font=("Helvetica", 12))
            choice_button.pack()
            self.choice_buttons.append(choice_button)

        next_button = tk.Button(self.master, text="Next", command=self.next_question, font=("Helvetica", 12))
        next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]

            self.question_label.config(text=current_question.question)

            choices = current_question.choices
            random.shuffle(choices)

            for i in range(4):
                self.choice_buttons[i].config(text=choices[i], value=choices[i])

        else:
            self.show_result()

    def next_question(self):
        selected_choice = self.choice_var.get()

        if selected_choice == "":
            messagebox.showinfo("Error", "Please select an answer.")
        else:
            current_question = self.questions[self.current_question_index]

            if selected_choice == current_question.choices[current_question.correct_choice - 1]:
                self.score += 1

            self.current_question_index += 1
            self.load_question()

    def show_result(self):
        result_message = f"You scored {self.score}/{len(self.questions)}!"
        messagebox.showinfo("Quiz Result", result_message)
        self.master.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

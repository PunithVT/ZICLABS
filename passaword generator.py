import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Initialize Tkinter variables
        self.characters_var = tk.StringVar(value="8")
        self.password_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        # Label and Entry for entering the number of characters
        tk.Label(self.master, text="Number of characters:").pack(pady=10)
        entry_characters = tk.Entry(self.master, textvariable=self.characters_var)
        entry_characters.pack()

        # Button to generate the password
        btn_generate = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        btn_generate.pack(pady=20)

        # Label to display the generated password
        tk.Label(self.master, text="Generated Password:").pack()
        entry_password = tk.Entry(self.master, textvariable=self.password_var, state="readonly")
        entry_password.pack()

    def generate_password(self):
        try:
            characters_number = int(self.characters_var.get())

            if characters_number < 8:
                messagebox.showinfo("Error", "Number of characters should be at least 8.")
            else:
                password = self.generate_strong_password(characters_number)
                self.password_var.set(password)
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid number.")

    def generate_strong_password(self, characters_number):
        s1 = list(string.ascii_lowercase)
        s2 = list(string.ascii_uppercase)
        s3 = list(string.digits)
        s4 = list(string.punctuation)

        random.shuffle(s1)
        random.shuffle(s2)
        random.shuffle(s3)
        random.shuffle(s4)

        part1 = min(round(characters_number * (30 / 100)), len(s1))
        part2 = min(round(characters_number * (20 / 100)), len(s3))

        result = []

        for x in range(part1):
            result.append(s1[x])
            result.append(s2[x])

        for x in range(part2):
            result.append(s3[x])
            result.append(s4[x])

        random.shuffle(result)

        return "".join(result)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



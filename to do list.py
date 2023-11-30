import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        # self.root.iconbitmap("icon.ico")  # Comment out or replace with an existing icon file

        self.tasks = []

        # Styling
        self.root.configure(bg="#f0f0f0")

        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")

        # Entry for adding tasks
        self.entry = tk.Entry(root, font=entry_font, bg="#fff", bd=2, relief=tk.SOLID)
        self.entry.pack(pady=10, padx=20, ipadx=10, fill=tk.X)

        # Button to add task
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=button_font, bg="#4CAF50", fg="#fff", bd=0, padx=10, pady=5)
        self.add_button.pack(pady=5)

        # Button to list tasks
        self.list_button = tk.Button(root, text="List Tasks", command=self.list_tasks, font=button_font, bg="#3498db", fg="#fff", bd=0, padx=10, pady=5)
        self.list_button.pack(pady=5)

        # Button to remove task
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=button_font, bg="#e74c3c", fg="#fff", bd=0, padx=10, pady=5)
        self.remove_button.pack(pady=5)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, selectbackground='#a6a6a6', selectmode=tk.SINGLE, font=entry_font, bd=0, bg="#f0f0f0", selectforeground="#fff", relief=tk.FLAT, height=10, width=40)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.X)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.entry.delete(0, tk.END)

    def list_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        if self.tasks:
            for task in self.tasks:
                self.tasks_listbox.insert(tk.END, task)
        else:
            self.tasks_listbox.insert(tk.END, "No tasks in the list.")

    def remove_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.list_tasks()

def main():
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


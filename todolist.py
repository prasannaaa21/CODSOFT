import tkinter as tk  ##USING TKINTER
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.root.configure(bg='#FF0000')  # Red background

        self.tasks = []

        # Title Label
        title_label = tk.Label(root, text="To-Do List", font=('Arial', 20), bg='#FF0000', fg='white')
        title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, font=('Arial', 12), width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        buttons = [("Add Task", self.add_task), ("Delete Task", self.delete_task),
                   ("Save Tasks", self.save_tasks), ("Load Tasks", self.load_tasks)]

        for text, command in buttons:
            button = tk.Button(root, text=text, command=command, font=('Arial', 12), bg='#FF0000', fg='white')
            button.pack(pady=10)

        # Task List
        self.task_listbox = tk.Listbox(root, selectbackground='#FF0000', selectforeground='white', font=('Arial', 12),
                                       bg='white', fg='#FF0000')
        self.task_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Thsi Function will perform addition of task
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()

    # This Function will perform deletion of task
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    # This Function will Save task
    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            file.write('\n'.join(self.tasks))

    # This Function will load task
    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as file:
                self.tasks = file.read().splitlines()
                self.update_task_list()
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "No saved tasks found.")

    # This function updates task
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

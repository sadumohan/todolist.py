import tkinter as tk
from tkinter import messagebox

class TodoList:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()

        self.mark_done_button = tk.Button(root, text="Mark Done", command=self.mark_done)
        self.mark_done_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]] = "[Done] " + self.tasks[selected_task_index[0]]
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("To-Do List", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_listbox()
            messagebox.showinfo("To-Do List", "Tasks loaded successfully!")
        except FileNotFoundError:
            messagebox.showerror("To-Do List", "No saved tasks found!")

if __name__ == "_main_":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
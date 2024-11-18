import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")
root.configure(bg="black")  # Set the background color to black

# Create and style the user interface elements
frame_tasks = tk.Frame(root, bg="black")
frame_tasks.place(relx=0.5, rely=0.1, anchor="n")

entry_task = tk.Entry(frame_tasks, width=30, font=("Arial", 14), bg="#333333", fg="#ffffff")
entry_task.pack(side=tk.LEFT, padx=5, pady=5)

button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#4CAF50",
    "fg": "white",
    "borderwidth": 0,
    "relief": "flat",
    "highlightthickness": 0,
    "padx": 10,
    "pady": 5
}

button_add_task = tk.Button(frame_tasks, text="Add Task", width=15, **button_style, command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5, pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=20, **button_style, command=delete_task)
button_delete_task.place(relx=0.5, rely=0.3, anchor="n")

listbox_tasks = tk.Listbox(root, width=50, height=15, font=("Arial", 12), bg="#333333", fg="#ffffff", selectbackground="#add8e6")
listbox_tasks.place(relx=0.5, rely=0.4, anchor="n")

# Run the application
root.mainloop()

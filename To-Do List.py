import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My To-Do list")
frame = tk.Frame(root)
frame.pack(pady=10)
tasks = []
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)
listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar and attach it to the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


def update_listbox():
    listbox.delete(0, tk.END)  # deletes all items in listbox from index 0 to tk.END
    for task in tasks:
        listbox.insert(tk.END, task)  # for each task in tasks, insert the task before tk.END


def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    selected_task_indices = listbox.curselection()  # curselection() returns a tuple of all elements that are selected
                                                    # from listbox.
    if not selected_task_indices:  # If no tasks were selected, show a warning
        messagebox.showwarning("Warning", "You must select a task to remove.")
        return
    # Loop through the selected indices in reverse order because if we loop forward while deleting, we change index
    # while needing to go to next index
    for index in reversed(selected_task_indices):
        listbox.delete(index)  # Remove the task from the Listbox
        tasks.pop(index)  # Remove the task from the tasks list


def clear_tasks():
    global tasks
    tasks = []
    update_listbox()


# Create a button to add tasks
add_task_button = tk.Button(
    root,
    text="Add Task",
    width=48,
    command=add_task
)
add_task_button.pack(pady=5)

# Create a button to delete selected tasks
delete_task_button = tk.Button(
    root,
    text="Delete Selected Task",
    width=48,
    command=delete_task
)
delete_task_button.pack(pady=5)

# Create a button to clear all tasks
clear_tasks_button = tk.Button(
    root,
    text="Clear All Tasks",
    width=48,
    command=clear_tasks
)
clear_tasks_button.pack(pady=5)

# Start the main loop
root.mainloop()

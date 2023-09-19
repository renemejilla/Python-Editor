import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)  # Clear the current text
            text.insert(tk.END, file.read())  # Insert the content of the file

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))  # Write the text to the file

# Create the main application window
root = tk.Tk()
root.title("ACMITS Text Editor")

# Create a text widget for editing
text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu = tk.Menu(menu_bar, tearoff=False)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu.add_command(label="Undo", command=edit_undo)

# Start the application
root.mainloop()





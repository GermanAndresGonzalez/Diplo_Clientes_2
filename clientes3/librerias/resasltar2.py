import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Treeview Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Age", "Country"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Country", text="Country")

# Insert some data
tree.insert("", "end", iid=0, values=("John", 25, "USA"))
tree.insert("", "end", iid=1, values=("Anna", 30, "UK"))

# Insert a value into a specific cell
tree.set(0, "Age", 26)  # Update John's age to 26

# Pack the Treeview widget
tree.pack()

# Run the application
root.mainloop()

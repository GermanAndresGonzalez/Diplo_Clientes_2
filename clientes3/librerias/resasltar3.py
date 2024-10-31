import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Treeview Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Column1", "Column2"), show="headings")
tree.heading("Column1", text="Column 1")
tree.heading("Column2", text="Column 2")

# Insert some data
tree.insert("", "end", values=("Row 1, Col 1", "Row 1, Col 2"))
tree.insert("", "end", values=("Row 2, Col 1", "Row 2, Col 2"))

# Pack the Treeview widget
tree.pack()


# Function to get coordinates of a selected item
def get_coordinates(event):
    selected_item = tree.selection()[0]
    item = tree.item(selected_item)
    print("Selected item:", item["values"])
    print("Coordinates:", tree.bbox(selected_item))


# Bind the Treeview widget to the function
tree.bind("<<TreeviewSelect>>", get_coordinates)

# Run the application
root.mainloop()

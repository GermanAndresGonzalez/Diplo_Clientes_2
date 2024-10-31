from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

# Create a Treeview widget
tree = ttk.Treeview(win, columns=("ID", "Company"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Company", text="Company")

# Insert some data
tree.insert("", "end", values=("1", "Honda"))
tree.insert("", "end", values=("2", "Hyundai"))
tree.insert("", "end", values=("3", "Tesla"))

tree.pack()


def edit_item():
    # Get selected item
    selected_item = tree.selection()[0]
    # Update the item
    tree.item(selected_item, values=("4", "Toyota"))


# Add a button to edit the selected item
edit_btn = ttk.Button(win, text="Edit", command=edit_item)
edit_btn.pack()

win.mainloop()

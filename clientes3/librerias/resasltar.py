import tkinter as tk
from tkinter import ttk


def highlight_cell(tree, row, column, bg="yellow", fg="black"):
    tree.tag_configure("highlight", background=bg, foreground=fg)
    tree.item(row, tags="highlight")


root = tk.Tk()
tree = ttk.Treeview(root, columns=("A", "B", "C"), show="headings")
tree.heading("A", text="Column A")
tree.heading("B", text="Column B")
tree.heading("C", text="Column C")

# Insert some data
tree.insert("", "end", iid=0, values=("1", "2", "3"))
tree.insert("", "end", iid=1, values=("4", "5", "6"))

# Highlight cell in row 0, column B
highlight_cell(tree, 0, "B")

tree.pack()
root.mainloop()

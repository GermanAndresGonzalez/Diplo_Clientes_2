import tkinter as tk
from tkinter import ttk
from referencia.referencia_treeview import referencia_tree

nombre_columnas = list(referencia_tree["nombre_columnas"])
claves = list(referencia_tree["nombre_columnas"].keys())


class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Double-1>", self.edit)

    def edit(self, event):
        self.editing = True
        self.event_generate("<<TreeviewEdit>>")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Treeview Example")
    tree = ttk.Treeview(root)

    columns = list(referencia_tree["nombre_columnas"].keys())[1:]
    tree["columns"] = columns

    tree.column("#0", width=10)
    tree.heading("#0", text="ID", anchor=tk.W)

    for col in columns:
        tree.column(col, anchor=tk.W, width=100)
        tree.heading(col, text=col, anchor=tk.W)
    tree.insert(parent="", index=tk.END, text="1")

    tree.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

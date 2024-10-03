import tkinter as tk
from tkinter import ttk
from referencia.referencia_treeview import referencia_tree

nombre_columnas = referencia_tree["nombre_columnas"]
print(nombre_columnas)


class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Double-1>", self.edit)

    def edit(self, event):
        self.editing = True
        self.event_generate("<<TreeviewEdit>>")


if __name__ == "__main__":
    root = tk.Tk()

    tree = TreeviewEdit(root, columns=nombre_columnas, show="headings", height=5)
    tree.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

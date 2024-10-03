class acercade(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("300x100")
        self.title("Toplevel Window")

        ttk.Button(self, text="Cerrar", command=self.destroy).pack(expand=True)

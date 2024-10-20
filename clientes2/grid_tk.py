import tkinter as tk

root = tk.Tk()
root.title("Columnconfigure Example")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Configuramos el Frame para que tenga 3 columnas
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

# Creamos algunos widgets para mostrar en las columnas
label1 = tk.Label(frame, text="Columna 1")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(frame, text="Columna 2")
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(frame, text="Columna 3")
label3.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()

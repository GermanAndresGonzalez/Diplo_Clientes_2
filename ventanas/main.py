import sqlite3
import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self):
        self.login_window = tk.Tk()
        self.login_window.title("Login App")
        self.login_window.geometry("300x200")

        tk.Label(self.login_window, text="usuario:").grid(row=0, column=0)
        tk.Label(self.login_window, text="contra:").grid(row=1, column=0)

        self.usuario_entry = tk.Entry(self.login_window)
        self.usuario_entry.grid(row=0, column=1)

        self.contra_entry = tk.Entry(self.login_window, show="*")
        self.contra_entry.grid(row=1, column=1)

        tk.Button(
            self.login_window,
            text="Login",
            command=self.login,
        ).grid(row=2, column=0)

        tk.Button(
            self.login_window,
            text="Register",
            command=self.register,
        ).grid(row=2, column=1)

        self.login_window.mainloop()

    def login(self):
        usuario = self.usuario_entry.get()
        contra = self.contra_entry.get()

        conn = sqlite3.connect("../clientes_nuevo.db")
        c = conn.cursor()
        c.execute('SELECT * FROM usuarios WHERE nombre_usuario = ? AND contrasena = ?', (usuario, contra))
        result = c.fetchone()

        if result:
            self.mostrar_datos(result)
            
        else:
            messagebox.showerror("Login", "Usuario or contraseña inválidos")

    def mostrar_datos(self,resultado):
        self.login_window.destroy()
        self.ventana_datos= tk.Tk()
        self.ventana_datos.title("Datos")
        self.ventana_datos.geometry("300x200")

        tk.Label(self.ventana_datos, text="usuario:").grid(row=0, column=0)
        tk.Label(self.ventana_datos, text="contra:").grid(row=1, column=0)
        tk.Label(self.ventana_datos, text="cocorreo_electronico:").grid(row=2, column=0)
        tk.Label(self.ventana_datos, text="nombre:").grid(row=3, column=0)

        tk.Label(self.ventana_datos, text=resultado[0]).grid(row=0, column=1)
        tk.Label(self.ventana_datos, text=resultado[1]).grid(row=1, column=1)
        tk.Label(self.ventana_datos, text=resultado[2]).grid(row=2, column=1)
        tk.Label(self.ventana_datos, text=resultado[3]).grid(row=3, column=1)

        tk.Button(
            self.ventana_datos,
            text="Close",
            command=self.ventana_datos.destroy,
        ).grid(row=4, column=0)

        
        self.ventana_datos.mainloop()
        
    def register(self):
                
        usuario = self.usuario_entry.get()
        contra = self.contra_entry.get()
        
        
if __name__ == "__main__":
    app = LoginApp()
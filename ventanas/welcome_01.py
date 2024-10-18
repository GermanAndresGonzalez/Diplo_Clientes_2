"""Página de bienvenida a la aplicación."""

import tkinter as tk


root = tk.Tk()
root.title("Bienvenido")
root.geometry("500x600")

bg_color = "#273b7a"
fuente_botones = ("Bold", 14)
fuente_labels = ("Bold", 14)
login_student_icon = tk.PhotoImage(file="ventanas/imagenes/login_student_img.png")
login_admin_icon = tk.PhotoImage(file="ventanas/imagenes/admin_img.png")
add_student_icon = tk.PhotoImage(file="ventanas/imagenes/add_student_img.png")


def welcome_page():
    welcome_page_fm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

    heading_lb = tk.Label(
        welcome_page_fm,
        bg=bg_color,
        fg="white",
        text="Bienvenido a la aplicación\n de manejo de Clientes",
        font=("Bold", 18),
        padx=10,
        pady=10,
    )
    heading_lb.place(x=0, y=0, width=400, height=70)

    student_login_btn = tk.Button(
        welcome_page_fm,
        text="Iniciar sesión Etudiantes",
        compound="left",
        font=fuente_botones,
        bg=bg_color,
        fg="white",
        bd=0,
    )
    student_login_btn.place(x=120, y=125, width=250, height=50)
    student_login_img = tk.Button(
        welcome_page_fm,
        image=login_student_icon,
        bd=0,
    )
    student_login_img.place(x=60, y=100)

    admin_login_btn = tk.Button(
        welcome_page_fm,
        text="Iniciar sesión Admin",
        compound="left",
        font=fuente_botones,
        bg=bg_color,
        fg="white",
        bd=0,
    )
    admin_login_btn.place(x=120, y=225, width=250, height=50)
    admin_login_img = tk.Button(
        welcome_page_fm,
        image=login_admin_icon,
        bd=0,
    )
    admin_login_img.place(x=60, y=200)

    add_student_btn = tk.Button(
        welcome_page_fm,
        text="Crear cuenta",
        compound="left",
        font=fuente_botones,
        bg=bg_color,
        fg="white",
        bd=0,
    )
    add_student_btn.place(x=120, y=325, width=250, height=50)

    add_student_img = tk.Button(
        welcome_page_fm,
        image=add_student_icon,
        bd=0,
    )
    add_student_img.place(x=60, y=300)

    welcome_page_fm.pack(pady=30)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=400, height=420)


student_login_page_fm = tk.Frame(
    root, highlightbackground=bg_color, highlightthickness=3
)
heading_lb = tk.Label(
    student_login_page_fm,
    text="Inicio sesion",
    bg=bg_color,
    fg="white",
    font=("Bold", 18),
    padx=10,
    pady=10,
)
heading_lb.place(x=0, y=0, width=400)

stud_icon_lb = tk.Label(
    student_login_page_fm,
    image=login_student_icon,
    bd=0,
)
stud_icon_lb.place(x=150, y=70)

id_number_lb = tk.Label(
    student_login_page_fm,
    text="Ingrese el número de client.",
    bg=bg_color,
    fg="white",
    font=("Bold", 14),
    padx=10,
    pady=10,
)
id_number_lb.place(x=100, y=100)

id_number_entry = tk.Entry(
    student_login_page_fm,
    font=("Bold", 14),
)


admin_icon_lb = tk.Label(
    student_login_page_fm,
    image=login_admin_icon,
    bd=0,
)
admin_icon_lb.place(x=60, y=200)

add_student_btn = tk.Button(
    student_login_page_fm,
    text="Crear cuenta",
    compound="left",
    font=fuente_botones,
    bg=bg_color,
    fg="white",
    bd=0,
)

student_login_page_fm.pack(pady=30)
student_login_page_fm.pack_propagate(False)
student_login_page_fm.configure(width=400, height=420)

# admin_login_page = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)
# add_student_page = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

root.mainloop()

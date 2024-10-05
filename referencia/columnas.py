import tkinter as tk

root = tk.Tk()

root.geometry("600x300")


canvas_1 = tk.Canvas(master=root, width=600, height=15)
canvas_2 = tk.Canvas(master=root)

canvas_1.pack(expand=True, fill="both")
canvas_2.pack(expand=True, fill="both")


#
frame_1 = tk.Frame(master=root)
frame_1.pack(expand=True, fill="both")

#  ------------------------------------------------------ All in row=0
button_in_column_0 = tk.Button(master=frame_1, text="I'm in Column_1").grid(
    row=0, column=1
)
button_in_column_1 = tk.Button(master=frame_1, text="I'm in Column_2", width=80).grid(
    row=0, column=2, columnspan=2
)
button_in_column_2 = tk.Button(master=frame_1, text="I'm in Column_3").grid(
    row=0, column=3
)

#  -----Let's say that you want the column 1 in the row 0 to expand if there is extra space
for x in range(2, 3):
    frame_1.columnconfigure(x, weight=1)
    frame_1.rowconfigure(x, weight=1)


#  LET CREATE THE SECOND LINE WITH LIST OF BUTTONS

frame_2 = tk.Frame(master=root)
frame_2.pack(expand=True, fill="both")

#  ------------------------------------------------------------ All in row=0
button_1 = tk.Button(master=frame_2, text="I'm in Column_Down").grid(
    row=0, column=1, sticky=tk.NSEW
)
button_2 = tk.Button(master=frame_2, text="I'm in Column_2").grid(
    row=0, column=2, sticky=tk.NSEW
)
button_3 = tk.Button(master=frame_2, text="I'm in Column_3").grid(
    row=0, column=3, sticky=tk.NSEW
)


window_1 = canvas_1.create_window(0, 1, anchor="nw", window=frame_1)
window_2 = canvas_2.create_window(0, 1, anchor="nw", window=frame_2)


root.mainloop()

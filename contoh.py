import tkinter as tk

window = tk.Tk()
window.geometry("800x600")

f1 = tk.Frame(window, background="pink", width=10, height=100)
f1.grid(row=0, column=0, sticky="nsew")

f2 = tk.Frame(window, background="cyan", width=10, height=100)
f2.grid(row=0, column=1, sticky="nsew")

window.grid_columnconfigure(0, weight=1)

window.grid_columnconfigure(1, weight=1)

window.grid_rowconfigure(0, weight=1)

window.mainloop()
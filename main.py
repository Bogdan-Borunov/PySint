import tkinter as tk
from functions import *

root = tk.Tk()
root.title("PySint")
root.geometry("620x800")
root.configure(bg = "black")
root.resizable(False, False)
Search = tk.BooleanVar()

logo = tk.Label(
    root,
    text="PySint",
    font=("Montserrat", 48, "bold"),
    fg="#50C900",
    bg="black"
)

logo.pack(pady=20)

InputText = tk.Label(root, text="Основной запрос:", fg="#50C900", bg="black", font=("Orbitron", 14, "bold"))
InputText.place(x=15, y=220)

Input = tk.Entry(root, bg="#282B26", selectbackground="#282B26", fg="#50C900", insertbackground="#50C900", font=("Arial", 14, "bold"))
Input.place(x=15, y=250)

Check = tk.Checkbutton(root, bg="black", fg="#50C900", text="Точный поиск (кавычки)", activebackground="#43473F", font=("Orbitron", 11, "bold"), variable=Search)
Check.place(x=380, y=250)

def run():
    query = Input.get()
    exact_search = Search.get()

    RunOsint(query, exact_search)

RunButton = tk.Button(root, text="Запуск ▶", fg="#50C900", bg="black", font=("Arial", 13, "bold"), command=run)
RunButton.place(x=15, y=700)

root.mainloop()
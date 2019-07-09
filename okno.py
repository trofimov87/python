from tkinter import *
from tkinter import messagebox
from datetime import date

class okno:
    def proverka(self):
        log = self.ent1.get()
        p = self.ent2.get()
        if log == "admin" and p == "admin":
            messagebox.showinfo("Отчёт!", "Логин и пароль введены верно!")
        else:
            messagebox.showinfo("Отчёт!", "Логин и пароль указаны неправильно!")

    def __init__(self):
        self.but = Button(root, text="OK", command=self.proverka)
        self.lab1 = Label(root, text="Login")
        self.ent1 = Entry(root, width=20, bd=3)
        self.lab2 = Label(root, text="Password")
        self.ent2 = Entry(root, width=20, bd=3)
        self.date = Label(root, text=date.today())
        self.date.grid(row=0, column=0)
        self.lab1.grid(row=1, column=0, sticky="w")
        self.ent1. grid(row=1, column=1, sticky="w")
        self.lab2.grid(row=2, column=0, sticky="w")
        self.ent2.grid(row=2, column=1, sticky="w")
        self.but.grid(row=3, column=1,  sticky="n")

root = Tk()
root.title("OKNO")
obj = okno()
root.mainloop()

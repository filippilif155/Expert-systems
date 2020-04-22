from tkinter import *
t = 0
class Cvor:
    def __init__(self, ime, cijena, dubina):
        self.ime = ime
        self.djeca = ()
        self.cijena = cijena
        self.dubina = dubina
        global t
        self.t = t

        self.w = 100 - self.dubina*10
        self.h = 60 - self.dubina*10
        self.y1 = 80 - self.dubina*10
        self.y2 = 60 - self.dubina*10
        self.txt_x = 43 - self.dubina*5
        self.txt_y = 30 - self.dubina*4.3
        self.font_size = 20 - self.dubina*3

        self.canvas = Canvas(main, width = self.w, height = self.h)
        if self.ime == "A":
            t = 4

        self.canvas.grid(row = self.dubina * 2 , column = t)
        self.canvas.create_oval(5, 5, self.y1, self.y2)
        self.canvas.create_text(self.txt_x, self.txt_y, fill = "black", font = f"Times {self.font_size} italic bold", text = self.ime)
        t += 1
    def promijeni_boju(self):
        self.canvas.create_oval(5, 5, self.y1, self.y2, fill='gray')
        self.canvas.create_text(self.txt_x, self.txt_y, fill = "black", font = f"Times {self.font_size} italic bold", text = self.ime)
    def dodaj_djecu(self, djeca, cijene, nl = 0):
        if nl == 0:
            global t
            t = 1
        print(self.ime)
        for (i, k) in enumerate(djeca):
            print(t)
            self.canvas = Canvas(main, width=30, height=30)
            self.canvas.grid(row=(self.dubina + 1) * 2, column=t)
            t+=1
            self.djeca += (Cvor(k, cijene[i], self.dubina + 1),)
            self.canvas = Canvas(main, width=self.w, height=self.h)
            self.canvas.grid(row=(self.dubina + 1), column=t)
            t+=1

        print("--------------")

class Stablo:
    def __init__(self, korijen):
        self.korijen = Cvor(korijen, 0, 0)

main = Tk()
main.title("Stablo")
main.geometry("900x900")
#Button(main, text = "Sledeca iteracija", width = 12, command = sl_iteracija()).grid(row = 0, column = 0, sticky = W)
X = Stablo("A")
line = Canvas(main, width=100, height=60)
line.grid(row=X.korijen.dubina * 2 + 1, column=t)
line.create_line(5, 5, 40, 60)
X.korijen.dodaj_djecu(("B", "C", "D"), (5, 9, 8))
X.korijen.djeca[0].dodaj_djecu(("E", "F"), (5, 11))
X.korijen.djeca[1].dodaj_djecu(("G",), (2,), 1)
X.korijen.djeca[2].dodaj_djecu(("H", "I", "J"), (11, 10, 7), 1)


X.korijen.djeca[0].djeca[0].dodaj_djecu(("K",), (8,))
X.korijen.djeca[0].djeca[1].dodaj_djecu(("L", "M"), (4, 1), 1)
X.korijen.djeca[2].djeca[0].dodaj_djecu(("N",), (5,), 1)
X.korijen.djeca[2].djeca[1].dodaj_djecu(("Cilj",), (2,), 1)
X.korijen.djeca[2].djeca[2].dodaj_djecu(("O",), (4,), 1)

X.korijen.djeca[0].djeca[0].djeca[0].dodaj_djecu(("Cilj", "Q"), (3, 7))
X.korijen.djeca[0].djeca[1].djeca[0].dodaj_djecu(("R",), (5,), 1)
X.korijen.djeca[2].djeca[0].djeca[0].dodaj_djecu(("S", "T"), (2, 3), 1)
X.korijen.djeca[2].djeca[2].djeca[0].dodaj_djecu(("U", "W"), (2, 1), 1)

'''
X.korijen.promijeni_boju()
X.korijen.pr_d()

X.korijen.djeca[0].pr_d()
X.korijen.djeca[1].pr_d()
X.korijen.djeca[2].pr_d()

X.korijen.djeca[0].djeca[0].pr_d()
X.korijen.djeca[0].djeca[1].pr_d()


X.korijen.djeca[2].djeca[0].pr_d()
X.korijen.djeca[2].djeca[1].pr_d()
X.korijen.djeca[2].djeca[2].pr_d()

X.korijen.djeca[0].djeca[0].djeca[0].pr_d()
X.korijen.djeca[0].djeca[1].djeca[0].pr_d()

X.korijen.djeca[2].djeca[0].djeca[0].pr_d()
X.korijen.djeca[2].djeca[2].djeca[0].pr_d()

canvas = Canvas(main, width=100, height=60)
canvas.grid(row=1, column=1)
canvas.create_oval(5, 5, 80, 60, fill="white")

'''
logo = PhotoImage(file="watch-1.png")
w1 = Label(main, image=logo).grid(row = 10, column = 0)

main.mainloop()
#X.korijen.djeca[0].djeca[0].dodaj_djecu(("D"))
#X.pr()

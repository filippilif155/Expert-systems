from tkinter import *
import time
class Cvor:
    def __init__(self, ime, cijena):
        self.ime = ime
        self.djeca = ()
        self.cijena = cijena

    def dodaj_djecu(self, djeca, cijene):
        for (i, k) in enumerate(djeca):
            self.djeca += (Cvor(k, cijene[i]),)

class Stablo:
    def __init__(self, korijen):
        self.korijen = Cvor(korijen, 0)
        self.iteracija = 0
        self.put = (("A", 0))
        self.trenutni_cvor = self.korijen

    def nadji_cilj(self):
        logo1 = PhotoImage(file=f"slika-{self.iteracija + 1}.png")
        w2 = Label(main, image=logo1)
        w2.img = logo1
        w2.grid(row = 1, column = 0)
        self.iteracija+=1


X = Stablo("A")
X.korijen.dodaj_djecu(("B", "C", "D"), (5, 9, 8))
X.korijen.djeca[0].dodaj_djecu(("E", "F"), (5, 11))
X.korijen.djeca[1].dodaj_djecu(("G",), (2,))
X.korijen.djeca[2].dodaj_djecu(("H", "I", "J"), (11, 10, 7))


X.korijen.djeca[0].djeca[0].dodaj_djecu(("K",), (8,))
X.korijen.djeca[0].djeca[1].dodaj_djecu(("L", "M"), (4, 1))
X.korijen.djeca[2].djeca[0].dodaj_djecu(("N",), (5,))
X.korijen.djeca[2].djeca[1].dodaj_djecu(("Cilj",), (2,))
X.korijen.djeca[2].djeca[2].dodaj_djecu(("O",), (4,))

X.korijen.djeca[0].djeca[0].djeca[0].dodaj_djecu(("Cilj", "Q"), (3, 7))
X.korijen.djeca[0].djeca[1].djeca[0].dodaj_djecu(("R",), (5,))
X.korijen.djeca[2].djeca[0].djeca[0].dodaj_djecu(("S", "T"), (2, 3))
X.korijen.djeca[2].djeca[2].djeca[0].dodaj_djecu(("U", "W"), (2, 1))



main = Tk()
main.title("Stablo")
main.geometry("580x400")
Button(main, text = "Sledeca iteracija", width = 12, command = X.nadji_cilj).grid(row = 0, column = 0)

main.mainloop()



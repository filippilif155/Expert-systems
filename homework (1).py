from tkinter import *

#graf dat u formi dictionary-a gdje je value niz sa susjednim cvorovima i cijenom puta
graf = {'S': [('A', 3), ('D', 10)],
        'A': [('D', 5), ('B', 4)],
        'B': [('C', 2), ('D', 6)],
        'D': [('E', 2)],
        'E': [('F', 4)],
        'F': [('G', 3)]
        }
#neusmjereni graf
graf2 = {'S': [('A', 3), ('D', 10)],
        'A': [('S', 3), ('D', 5), ('B', 4)],
        'D': [('S', 10), ('A', 5), ('B', 6), ('E', 2)],
        'B': [('A', 4), ('C', 2), ('D', 6)],
        'C': [('B', 2)],
        'E': [('D', 2), ('F', 4)],
        'F': [('E', 4), ('G', 3)],
        'G' : [('F', 3)]
        }
#crtanje grafa (gui - biblioteka tkinter)
def stampaj(niz, boja_1, boja_2, line_width):
    main = Tk()
    main.title("Graf")
    main.geometry("674x900+0+0")

#za svaku iteraciju crtaju se otvoreni cvorovi
#elipse ispitanh cvorova zatamnjene, ukupna cijena putanje prikazana na poslednje cvoru
    for i, j in enumerate(niz):
        k = 0
        for t, x in enumerate(j[0]):
            if t != len(j[0]) - 1:
                canvas = Canvas(main, width = 70, height = 70)
                canvas.grid(row = k, column = i)
                canvas.create_oval(5, 5, 70, 50, fill = boja_1, width = line_width)
                canvas.create_text(35, 25, fill = "black", font="Times 20 italic bold", text = x)
                k += 1
                line = Canvas(main, width = 70, height = 30)
                line.grid(row = k, column = i)
                line.create_line(37, 0, 37, 30, width = line_width)
                k += 1
            else:
                canvas = Canvas(main, width=70, height=70)
                canvas.grid(row=k, column=i)
                canvas.create_oval(5, 5, 70, 50, fill = boja_2, width = line_width)
                canvas.create_text(35, 25, fill="black", font="Times 20 italic bold", text=x)
                canvas.create_text(56, 10, fill="black", font="Times 20 italic bold", text=j[1])

    #ukoliko korisnik sam upravlja iteracijama, koristi x na prozoru, a iduca linija se zakomentarise
    #main.after(3000, main.destroy) #nakon 3 sekunde zatvara se stari prozor i otvara novi za iducu iteraciju
    main.mainloop()

def uniformno_pretrazivanje(graf, pocetak, cilj):
    ispitani = [] 
    otvoreni = [[[pocetak], 0]]
    trenutni_cvor = pocetak
    potencijalni_put = [[pocetak], 0]
    najkraci_put = None
    brojac=0
    while najkraci_put == None and brojac<50: 
        brojac+=1 #ukoliko nakon 50 iteracija ne nadje cilj, izlazi iz petlje
        if trenutni_cvor != cilj:

            #izbjegavamo ponovljena stanja
            if trenutni_cvor in ispitani:
                for elem in otvoreni:
                    if elem[0][-1] in elem[0][0 : -1]:
                        otvoreni.remove(elem)
                ispitani.remove(trenutni_cvor)
                potencijalni_put = otvoreni[0]
                trenutni_cvor = potencijalni_put[0][-1]
                continue

            stampaj(otvoreni, "gray", "white", 1)
            otvoreni.remove(potencijalni_put)
            ispitani.append(trenutni_cvor)

            #namijenjen usmjerenim grafovima, ukoliko susjedi cvora nisu definisani
            try:
                graf[trenutni_cvor]
            except KeyError:
                potencijalni_put = otvoreni[0]
                continue

            for i in graf[trenutni_cvor]:
                pom = list(potencijalni_put[0])
                pom.append(i[0])
                otvoreni.append([pom, potencijalni_put[1] + i[1]])
            otvoreni = sorted(otvoreni, key=lambda i: i[1])
            potencijalni_put = otvoreni[0]
            trenutni_cvor = potencijalni_put[0][-1]
            if trenutni_cvor == cilj:
                najkraci_put = potencijalni_put
                stampaj([otvoreni[0]], "grey", "grey", 2) #cilj se nalazi u sortiranoj listi otvoreni, na prvom mjestu, samo on ostane prikazan
                return najkraci_put

#print(uniformno_pretrazivanje(graf, 'S', 'G'))
print(uniformno_pretrazivanje(graf2, 'S', 'G'))
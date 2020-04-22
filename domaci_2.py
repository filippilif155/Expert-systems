import random
import time
import matplotlib.pyplot as plt

def nacrtaj(matrica):
    fig, ax = plt.subplots()
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    x = ax.table(cellText=matrica, loc='center', cellLoc='center')
    x.set_fontsize(18)
    x.scale(1, 3)
    fig.tight_layout()
    plt.show()


def random_matrica():
    matrica = [[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
    for x in matrica:
        x[random.randrange(8)] = "Q"

    return matrica
def heuristika(matrica):
    heuristika = 0
    for i, red in enumerate(matrica):
        for j, elem in enumerate(red):
            kolona = j
            if elem == "Q":
                #kolone
                for r, elem_pom in enumerate(matrica):
                    if r > i:
                        if elem_pom[kolona] == "Q":
                            heuristika += 1
                # dijagonala dolje lijevo
                kolona = j - 1
                for r, elem_pom in enumerate(matrica):
                    if r > i:
                        if kolona >= 0 and elem_pom[kolona] == "Q":
                            heuristika += 1
                        kolona -= 1
                kolona = j + 1
                # dijagonala dolje desno
                for r, elem_pom in enumerate(matrica):
                    if r > i:
                        if kolona < 8 and elem_pom[kolona] == "Q":
                            heuristika += 1
                        kolona += 1
    return heuristika

def heuristika_matrice(matrica):
    for i, x in enumerate(matrica):
        for j, y in enumerate(x):
            kolona = j
            if y != "Q":
                matrica_pom = []
                for k, t in enumerate(matrica):
                    matrica_pom.append(matrica[k].copy())
                matrica_pom[i][matrica_pom[i].index("Q")] = 0
                matrica_pom[i][j] = "Q"
                matrica[i][j] = heuristika(matrica_pom)
    return matrica

def planinarenje(tabla = 0):
    rjesenje = 0
    brojac = 0
    while rjesenje == 0:
        matrica = random_matrica()
        #crtanje prvi put
        if tabla == 1:
            nacrtaj(heuristika_matrice(matrica))
            time.sleep(2)

        while True:

            heuristika_trenutna = heuristika(matrica)
            matrica = heuristika_matrice(matrica)
            heuristika_min = heuristika_trenutna


            lista_heuristika = []
            for x in matrica:
                for y in x:
                    if(y != "Q" and y < heuristika_min):
                        heuristika_min = y

            for i, x in enumerate(matrica):
                for j, y in enumerate(x):
                    if(y != "Q" and y == heuristika_min):
                        lista_heuristika.append((i, j))
            if len(lista_heuristika) > 0:
                a, b = lista_heuristika[random.randrange(len(lista_heuristika))]
                matrica[a][matrica[a].index("Q")] = "X"
                matrica[a][b] = "Q"
            #crtanje
            if tabla == 1:
                nacrtaj(matrica)
                time.sleep(2)

            if heuristika_min >= heuristika_trenutna:
                brojac += 1
                break
            elif heuristika_min == 0:
                brojac += 1
                rjesenje = 1
                break

    return brojac



planinarenje(1)

brojaci_svi = 0
'''
for i in range(0, 200):
    brojaci_svi += planinarenje()
print(200/brojaci_svi)
print(brojaci_svi/200)
'''

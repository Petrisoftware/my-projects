# Petri Kemppinen 2019
# Subigeneraattori

# Generoi käyttäjälle satunnaisen Subway-subin.
# Valitsee yhden leivän, yhden täytteen ja satunnaisen määrän kasviksia ja
# kastikkeita.

import random

# Tiedostot, jotka ohjelman täytyy lukea.
FILES = ["leipa.txt", "tayte.txt", "kasvis.txt", "kastike.txt", "kuivat.txt"]


# Tarkistetaan, että kaikki tiedostot ovat olemassa.
def checkfiles():
    try:
        for file in FILES:
            f = open(file, 'r')
            f.close()
        return True
    except OSError:
        return False


# Lukee ainesosat tiedostoista ja tallettaa ne listaan.
def readfiles(aines):
    # Lue tiedosto riippuen siitä, mikä lista on kyseessä.
    lista = []
    f = open(aines, 'r', encoding="utf-8")
    for line in f:
        line = line.strip()
        lista.append(line)
    f.close()

    return lista


# Arpoo satunnaisen alkion annetusta listasta.
def randomitem(lista):
    itemno = random.randint(0, len(lista)-1)
    item = lista[itemno]
    return item


# Arpoo satunnaisen määrän alkioita annetusta listasta ja palauttaa ne listana.
def randomlist(lista):
    listsize = random.randint(0, len(lista)-1)
    listb = []
    for i in range(listsize):
        newitem = randomitem(lista)
        if newitem not in listb:
            listb.append(newitem)
        else:
            # On jo listassa.
            pass
    return listb


# Tulostetaan lista hieman siistimmällä tavalla.
def printlist(lista):
    listprint = ""
    for item in lista:
        listprint += (item + ", ")
    listprint = listprint.strip(', ')
    return listprint


def main():
    # Tervetuloa.
    print("Welcome to Subway Generator 2019")

    # Tarkistetaan tiedostojen olemassaolo.
    if checkfiles():
        print("All files present.")
    else:
        print("Error! Some files are missing.")

    # Luetaan ainesosat tiedostoista.
    leipa = readfiles("leipa.txt")
    tayte = readfiles("tayte.txt")
    kasvis = readfiles("kasvis.txt")
    kastike = readfiles("kastike.txt")
    kuivat = readfiles("kuivat.txt")

    # Seed satunnaisgeneraattorille.
    seed = input("Enter value for random generator: ")
    random.seed(seed)

    # Arvotaan subin täytteet.
    bread = randomitem(leipa)
    filling = randomitem(tayte)
    greens = randomlist(kasvis)
    sauces = randomlist(kastike)
    spices = randomlist(kuivat)

    # Kerrotaan käyttäjälle mitä tuli arvottua.
    print("\nLeipä:", bread)
    print("Täyte:", filling)
    print("Kasvikset:", printlist(greens))
    print("Kastikkeet:", printlist(sauces))
    print("Mausteet:", printlist(spices))

    return


main()

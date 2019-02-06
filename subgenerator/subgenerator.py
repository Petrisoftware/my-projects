# Petri Kemppinen 2019
# Subigeneraattori

# Generoi käyttäjälle satunnaisen Subway-subin.
# Valitsee yhden leivän, yhden täytteen ja satunnaisen määrän kasviksia ja
# kastikkeita.

import random

# Tiedostot, jotka ohjelman täytyy lukea.
FILES = ["leipa.txt", "tayte.txt", "kasvis.txt", "kastike.txt"]


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
    f = open(aines, 'r')
    for line in f:
        lista.append(line)
    f.close()

    return lista


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

    # Seed satunnaisgeneraattorille.
    seed = input("Enter value for random generator: ")
    random.seed(seed)

    # TODO: arvonta

    return


main()

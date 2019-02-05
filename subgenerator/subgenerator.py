# Petri Kemppinen 2019
# Subigeneraattori

# Generoi käyttäjälle satunnaisen Subway-subin.
# Valitsee yhden leivän, yhden täytteen ja satunnaisen määrän kasviksia ja
# kastikkeita.

import random

# Tiedostot, jotka ohjelman täytyy lukea.
FILES = ["leipa.txt", "tayte.txt", "kasvis.txt", "kastike.txt"]


# Lukee ainesosat tiedostoista ja tallettaa ne listaan.
def readfiles(lista, aines):
    # Lue lista riippuen siitä, mikä on kyseessä.
    if aines == "leipa":
        try:
            f = open("leipa.txt", 'r')
            f.close()
        except OSError:
            print("Error! File leipa.txt not found!")
    elif aines == "tayte":
        # eeee
    elif aines == "kasvis":
        # aaa
    elif aines == "kastike":
        # uliuliuli
    else:
        print("This shouldn't happen.")

    return lista


def main():
    # Tervetuloa.
    print("Welcome to Subway Generator 2019")

    # Luetaan ainesosat tiedostoista.
    leipa = []
    tayte = []
    kasvis = []
    kastike = []

    # Seed satunnaisgeneraattorille.
    seed = input("Enter value for random generator: ")
    random.seed(seed)

    # TODO: arvonta

    return


main()

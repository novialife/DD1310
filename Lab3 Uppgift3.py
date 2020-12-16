import random

Kast = int(input("Hur många kast behövs i spelet?  "))
Tarningar = int(input("Hur många tärningar behövs? "))


def spel():
    Resultat = []
    Omgang = 2
    i = 1
    while i < Tarningar + 1:
        Svar = random.randint(1, 6)
        Resultat.append(Svar)
        print("Tärning " + str(i) + ": " + str(Svar))
        i += 1

    S = ""
    for x in Resultat:
        S += str(x)
        S += ","
    print("Du fick " + S.strip(',') + ".")

    while Omgang <= Kast:
        cont = input("Vill du spela igen?j/n")
        if cont == "J" or cont == "j":
            Resultat.clear()
            i = 1
            while i < Tarningar + 1:
                Svar = random.randint(1, 6)
                Resultat.append(Svar)
                print("Tärning " + str(i) + ": " + str(Svar))
                i += 1

            S = ""
            for x in Resultat:
                S += str(x)
                S += ","
            print("Du fick " + S.strip(',') + ".")

            Omgang += 1

        elif cont == "N" or cont == "n":
            S = ""
            for x in Resultat:
                S += str(x)
                S += ","
            print("Du fick " + S.strip(',') + ".")
            break


while True:
    svar = input("Press enter to start or A to quit")
    if svar == "":
        spel()
        continue
    elif svar == "A" or svar == "a":
        break

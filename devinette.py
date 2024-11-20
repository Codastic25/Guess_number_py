from random import *

def devinette(start, end, essais):
    bot = randint(start, end)
    print("Essai gratuit: ")
    player = int(input("Ton nombre: "))

    if player < start:
        print("Nombre en dessous du minimum...Fin de jeu")
        return IndexError
    elif player > end:
        print("Nombre au dessus du maximum...Fin de jeu")
        return IndexError

    while player != bot and essais != 0:
        print("Try again !")
        essais -= 1
        print("Il te reste ", essais+1, "essais !")
        player = int(input("Ton nombre: "))

        if player > bot:
            print("Trop haut !")
        elif player < bot:
            print("Trop bas !")

    if essais == 0:
        print("Perdu ! Le nombre était: ", bot)
        return 0

    if player == bot:
        print("GG")
        return 1


#arg1 = min
#agr2 = max
#arg3 = nb d'essais
devinette(1, 100, 10)
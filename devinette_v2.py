import pygame
from random import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill(color="white")
pygame.display.set_caption("Guess number Game")

"""
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
"""


text = "Devinez le nombre !"
consigne = "Entrez un numéro entre 0 et 150 inclus: "
input_user = ""
erreur = "ERREUR"
indice_bas = "Vise plus haut !"
indice_haut = "Vise plus bas !"
loose = "PERDU !"
victoire = "GAGNE !"
indice = ""


bot = randint(0,150)

font = pygame.font.Font(None, 30)

text_color = (0,0,0)
erreur_color = (255,0,0)

pdv = 6

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():  # Vérifie si la touche est un chiffre
                input_user += event.unicode  # Ajoute le chiffre à input_user

            if event.key == pygame.K_BACKSPACE:  # Supprimer le dernier chiffre
                input_user = input_user[:-1]


            if event.key == pygame.K_RETURN:  # Si l'utilisateur appuie sur "Entrée"
                if input_user:  # Vérifie si input_user n'est pas vide
                    user_number = int(input_user)
                    if user_number < 0 or user_number > 150:
                        indice = erreur

                    else:
                        print(f"Numéro entré : {user_number}")# sur la console 

                    if user_number < bot:
                        indice = indice_bas
                        pdv -= 1
                    elif user_number > bot:
                        indice = indice_haut
                        pdv -= 1
                    elif user_number == bot:
                        screen.fill(color="green")

                        indice = victoire

                        font = pygame.font.Font(None, 80)
                        text_surface = font.render(indice, True, (255,255,255))
                        screen.blit(text_surface, (200, 250))
                        pygame.display.flip()

                        pygame.time.delay(6000)
                        running = False



                input_user = ""  # Réinitialiser après la validation (optionnel)

        if pdv == 0:
            screen.fill(color="red")

            indice = loose

            font = pygame.font.Font(None, 80)
            text_surface = font.render(indice, True, (255,255,255))
            screen.blit(text_surface, (200, 250))
            pygame.display.flip()

            pygame.time.delay(6000)
            running = False

    screen.fill(color="yellow")


    # Affichage du texte et des consignes
    screen.blit(font.render(consigne, True, text_color), (130, 100))
    screen.blit(font.render(text, True, text_color), (220, 50))
    screen.blit(font.render(input_user, True, text_color), (300, 160))

    #On affiche l'indice actuel
    screen.blit(font.render(indice, True, text_color if indice != erreur else (255,0,0)), (220, 300))

    #afficher le résultat
    #screen.blit(font.render(f"Le nombre aléatoire est : {bot}", True, text_color), (220, 400))

    #afficher les pdv du joueur
    screen.blit(font.render(f"pdv : {pdv}", True, text_color), (500, 550))

    # Mise à jour de l'affichage
    pygame.display.update()

pygame.quit()
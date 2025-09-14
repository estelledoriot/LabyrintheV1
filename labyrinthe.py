"""Estelle Doriot
Labyrinthe avec Pygame
Pikachu doit atteindre la pokéball sans toucher les murs du labyrinthe.
"""

import pygame

pygame.init()

# couleurs
jaune = (255, 255, 0)
bleu = (0, 0, 255)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
noir = (0, 0, 0)

# fenêtre
taille = (550, 550)
fenetre = pygame.display.set_mode(taille)
pygame.display.set_caption("Labyrinthe")
pygame.display.set_icon(pygame.image.load("pika.png"))

# labyrinthe
laby = pygame.image.load("laby.png")
labyR = laby.get_rect(center=(275, 275))

# pikachu
pika = pygame.image.load("pika.png")
pika = pygame.transform.scale(pika, (23, 25))
pikaR = pika.get_rect()
pikaR = pikaR.move(20, 415)

# pokeball
poke = pygame.image.load("pokeball.png")
poke = pygame.transform.scale(poke, (20, 20))
pokeR = poke.get_rect()
pokeR = pokeR.move(510, 110)

# gagné
police = pygame.font.Font("PermanentMarker-Regular.ttf", 100)
gagne = police.render("Gagné !!!", True, rouge)
gagneR = gagne.get_rect(center=(275, 200))

# rejouer
police2 = pygame.font.Font("Montserrat-VariableFont_wght.ttf", 50)
rejouer = police2.render("Rejouer", True, noir)
rejouerR = rejouer.get_rect(center=(275, 400))
bouton = rejouerR.inflate(15, 15)
bouton.center = (275, 400)

quitter = False
fini = False


def afficher_jeu():
    fenetre.fill(blanc)
    fenetre.blit(laby, labyR)
    fenetre.blit(pika, pikaR)
    fenetre.blit(poke, pokeR)


def afficher_menu():
    fenetre.fill(blanc)
    fenetre.blit(gagne, gagneR)
    pos = pygame.mouse.get_pos()
    couleur = bleu if bouton.collidepoint(pos) else noir
    rejouer = police2.render("Rejouer", True, couleur)
    pygame.draw.rect(fenetre, couleur, bouton, 1)
    fenetre.blit(rejouer, rejouerR)


afficher_jeu()

while not quitter:
    for evenement in pygame.event.get():
        # quitter
        if evenement.type == pygame.QUIT:
            quitter = True
            break
        # bouger pikachu
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_RIGHT:
                pikaR = pikaR.move(10, 0)
            if evenement.key == pygame.K_LEFT:
                pikaR = pikaR.move(-10, 0)
            if evenement.key == pygame.K_UP:
                pikaR = pikaR.move(0, -10)
            if evenement.key == pygame.K_DOWN:
                pikaR = pikaR.move(0, 10)
        # cliquer sur le bouton
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if bouton.collidepoint(pos):
                fini = False
                pikaR.x = 20
                pikaR.y = 415

    # fin de la partie
    if pikaR.colliderect(pokeR):
        fini = True

    # test de collision avec le labyrinthe
    labyForme = pygame.mask.from_surface(laby)
    pikaForme = pygame.mask.from_surface(pika)
    if labyForme.overlap_area(pikaForme, (pikaR.x - labyR.x, pikaR.y - labyR.y)):
        pikaR.x = 20
        pikaR.y = 415

    if not fini:
        afficher_jeu()
    else:
        afficher_menu()

    pygame.display.update()

pygame.quit()

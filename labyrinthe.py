from pygame import *

init()

# couleurs
jaune = (255,255,0)
bleu = (0,0,255)
blanc = (255,255,255)
rouge = (255,0,0)
vert = (0,255,0)
noir = (0,0,0)

# fenêtre
taille = (550, 550)
fenetre = display.set_mode(taille)
display.set_caption("Labyrinthe")
display.set_icon(image.load("pika.png"))

# labyrinthe
laby = image.load("laby.png")
labyR = laby.get_rect(center=(275,275))

# pikachu
pika = image.load("pika.png")
pika = transform.scale(pika,(23,25))
pikaR = pika.get_rect()
pikaR = pikaR.move(20,415)

# pokeball
poke = image.load("pokeball.png")
poke = transform.scale(poke,(20,20))
pokeR = poke.get_rect()
pokeR = pokeR.move(510,110)

# gagné
police = font.Font("PermanentMarker-Regular.ttf", 100)
gagné = police.render("Gagné !!!", 1, rouge)
gagnéR = gagné.get_rect(center=(275,200))

# rejouer
police2 = font.Font("Montserrat-VariableFont_wght.ttf", 50)
rejouer = police2.render("Rejouer", 1, noir)
rejouerR = rejouer.get_rect(center=(275,400))
bouton = rejouerR.inflate(15,15)
bouton.center = (275,400)

quitter = False
fini = False

def afficher_jeu():
    fenetre.fill(blanc)
    fenetre.blit(laby,labyR)
    fenetre.blit(pika,pikaR)
    fenetre.blit(poke,pokeR)

def afficher_menu():
    fenetre.fill(blanc)
    fenetre.blit(gagné,gagnéR)
    pos = mouse.get_pos()
    if bouton.collidepoint(pos):
        couleur = bleu
    else:
        couleur = noir
    rejouer = police2.render("Rejouer", 1, couleur)
    draw.rect(fenetre, couleur, bouton, 1)
    fenetre.blit(rejouer, rejouerR)

afficher_jeu()

while not quitter:
    for evenement in event.get(): 
        # quitter
        if evenement.type == QUIT:
            quitter = True
            break
        # bouger pikachu
        if evenement.type == KEYDOWN:
            if evenement.key == K_RIGHT:
                pikaR = pikaR.move(10,0)
            if evenement.key == K_LEFT:
                pikaR = pikaR.move(-10,0)
            if evenement.key == K_UP:
                pikaR = pikaR.move(0,-10)
            if evenement.key == K_DOWN:
                pikaR = pikaR.move(0,10)
        # cliquer sur le bouton
        if evenement.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            if bouton.collidepoint(pos):
                fini = False
                pikaR.x = 20
                pikaR.y = 415
    
    # fin de la partie
    if pikaR.colliderect(pokeR):
        fini = True
    
    # test de collision avec le labyrinthe
    labyForme = mask.from_surface(laby)
    pikaForme = mask.from_surface(pika)
    if labyForme.overlap_area(pikaForme,(pikaR.x-labyR.x,pikaR.y-labyR.y)):
        pikaR.x = 20
        pikaR.y = 415
    
    if not fini:
        afficher_jeu()
    else :
        afficher_menu()
        
    display.update()
    
quit()
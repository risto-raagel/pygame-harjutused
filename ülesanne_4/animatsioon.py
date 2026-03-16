import pygame
import sys
import random

# 1. Mängu algistamine
pygame.init()

# Ekraani seaded 640x480)
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Rallimäng - Lihtsustatud")

# Kell
clock = pygame.time.Clock()

# 2. Graafika laadimine ja suuruse muutmine (50x120)
taust = pygame.image.load("bg_rally.jpg")

# Punane auto
punane_auto_laetud = pygame.image.load("f1_red.png")
punane_auto = pygame.transform.scale(punane_auto_laetud, (40, 100))

# Sinine auto
sinine_auto_laetud = pygame.image.load("f1_blue.png")
sinine_auto = pygame.transform.scale(sinine_auto_laetud, (40, 100))

# Skoori algseis
skoor = 0
font = pygame.font.SysFont("Arial", 30)

# 3. Punase auto asukoht ekraani all keskel
playerX = screenX / 2 - punane_auto.get_rect().width / 2
playerY = screenY - punane_auto.get_rect().height - 10

# 4. Siniste autode loomine (X-koordinaat, Y-koordinaat, kiirus)
vastased = []
for i in range(4):
    vastaneX = random.choice([170, 430])  # Ainult vasak ja parem rada
    vastaneY = random.randint(-600, -150)  # Alustavad erinevatelt kõrgustelt
    kiirus = random.randint(4, 7)
    vastased.append([vastaneX, vastaneY, kiirus])

# 5. Mängutsükkel
gameover = False
while not gameover:
    clock.tick(60)  # Hoiame mängu kiiruse ühtlasena

    # Akna sulgemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # JOONISTAMINE
    # 1. Taust (puhastab ekraani väreluse vältimiseks)
    screen.blit(taust, (0, 0))

    # 2. Siniste autode liigutamine ja kuvamine
    for i in range(len(vastased)):
        # Liigutame autot ainult kiiruse võrra
        vastased[i][1] += vastased[i][2]

        # Kuvame sinise auto (asukoht peab olema täisarv)
        screen.blit(sinine_auto, (int(vastased[i][0] - 25), int(vastased[i][1])))

        # Kui auto jõuab alla, lisatakse punkt ja ta alustab uuesti
        if vastased[i][1] > screenY:
            vastased[i][1] = random.randint(-400, -150)
            vastased[i][0] = random.choice([170, 430])
            skoor += 1

    # 3. Punase auto kuvamine
    screen.blit(punane_auto, (int(playerX), int(playerY)))

    # 4. Skoori kuvamine (arv tuleb teisendada tekstiks str(number) abil)
    skoor_tekst = font.render("Skoor: " + str(skoor), True, [255, 255, 255])
    screen.blit(skoor_tekst, (10, 10))

    # Uuendame ekraani
    pygame.display.flip()

pygame.quit()
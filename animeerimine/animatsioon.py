import pygame
import random

# Käivitame pygame'i
pygame.init()

# Akna suurus
laius = 640
korgus = 480
aken = pygame.display.set_mode((laius, korgus))
pygame.display.set_caption("Vastutulevad autod")

# Värvid
valge = (255, 255, 255)

# Piltide laadimine
taust = pygame.image.load("bg_rally.jpg")
punane_auto_pilt = pygame.image.load("f1_red.png")
sinine_auto_pilt = pygame.image.load("f1_blue.png")

# Piltide suurused
taust = pygame.transform.scale(taust, (laius, korgus))
punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, (80, 120))
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, (80, 120))

# Fond ja skoor
font = pygame.font.SysFont(None, 36)
skoor = 0

# Punane auto
punane_laius = 80
punane_korgus = 120
punane_x = laius // 2 - punane_laius // 2
punane_y = korgus - 130

# -----------------------------------
# RAJAD TEE PEAL
# -----------------------------------
# Muuda neid väärtusi siis, kui autod ei jää õigesti tee peale.
# Need on siniste autode võimalikud x-asukohad.
koik_rajad = [170, 270, 370]

# Jätame punase auto rea vabaks
ohutud_rajad = []

for rada in koik_rajad:
    if abs(rada - punane_x) > 70:
        ohutud_rajad.append(rada)

# -----------------------------------
# SINISED AUTOD
# -----------------------------------
sinised_autod = []
autode_arv = 3
vahemaa = 140  # minimaalne vahe siniste autode vahel samal rajal

for i in range(autode_arv):
    while True:
        uus_x = random.choice(ohutud_rajad)
        uus_y = random.randint(-500, -120)
        uus_kiirus = random.randint(4, 7)

        sobib = True

        # Kontrollime, et uus auto ei oleks teise sinise autoga
        # samal rajal liiga lähedal
        for auto in sinised_autod:
            if uus_x == auto["x"] and abs(uus_y - auto["y"]) < vahemaa:
                sobib = False

        if sobib:
            auto = {
                "x": uus_x,
                "y": uus_y,
                "kiirus": uus_kiirus
            }
            sinised_autod.append(auto)
            break

# Kell
kell = pygame.time.Clock()

# Peatsükkel
kaib = True
while kaib:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kaib = False

    # Joonistame tausta
    aken.blit(taust, (0, 0))

    # Joonistame punase auto
    aken.blit(punane_auto_pilt, (punane_x, punane_y))

    # Siniste autode liikumine
    for i in range(len(sinised_autod)):
        auto = sinised_autod[i]

        # Joonistame sinise auto
        aken.blit(sinine_auto_pilt, (auto["x"], auto["y"]))

        # Liigutame autot alla
        auto["y"] += auto["kiirus"]

        # Kui auto jõuab alla, paneme ta uuesti üles
        if auto["y"] > korgus:
            skoor += 1

            while True:
                uus_x = random.choice(ohutud_rajad)
                uus_y = random.randint(-300, -120)
                uus_kiirus = random.randint(4, 7)

                sobib = True

                # Kontrollime, et uus auto ei tekiks samale rajale
                # teisele sinisele autole liiga lähedale
                for j in range(len(sinised_autod)):
                    teine_auto = sinised_autod[j]

                    if i != j:
                        if uus_x == teine_auto["x"] and abs(uus_y - teine_auto["y"]) < vahemaa:
                            sobib = False

                if sobib:
                    auto["x"] = uus_x
                    auto["y"] = uus_y
                    auto["kiirus"] = uus_kiirus
                    break

    # Skoori kuvamine
    skoori_tekst = font.render("Skoor: " + str(skoor), True, valge)
    aken.blit(skoori_tekst, (20, 20))

    # Ekraani uuendamine
    pygame.display.update()
    kell.tick(60)

pygame.quit()
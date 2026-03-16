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
must = (0, 0, 0)

# Piltide laadimine
taust = pygame.image.load("bg_rally.jpg")
punane_auto_pilt = pygame.image.load("f1_red.png")
sinine_auto_pilt = pygame.image.load("f1_blue.png")

# Piltide suurused
taust = pygame.transform.scale(taust, (laius, korgus))
punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, (60, 100))
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, (60, 100))

# Fond ja skoor
font = pygame.font.SysFont(None, 36)
skoor = 0

# Punane auto
punane_laius = 60
punane_korgus = 100
punane_x = laius // 2 - punane_laius // 2
punane_y = korgus - 130

# Rajad tee peal
koik_rajad = [170, 270, 410]

# Jätame punase auto rea täitsa vabaks
ohutud_rajad = []

for rada in koik_rajad:
    if abs(rada - punane_x) > 70:
        ohutud_rajad.append(rada)

# Sinised autod
sinised_autod = []
autode_arv = 3
vahemaa = 140


# Funktsioon, mis proovib leida uuele sinisele autole sobiva koha
def loo_uus_auto(olemasolevad_autod, auto_index=-1):
    for katse in range(100):  # proovime maksimaalselt 100 korda
        uus_x = random.choice(ohutud_rajad)
        uus_y = random.randint(-600, -120)   # suurem ala kui enne
        uus_kiirus = random.randint(4, 7)

        sobib = True

        for j in range(len(olemasolevad_autod)):
            if j == auto_index:
                continue

            teine_auto = olemasolevad_autod[j]

            if uus_x == teine_auto["x"] and abs(uus_y - teine_auto["y"]) < vahemaa:
                sobib = False
                break

        if sobib:
            return {
                "x": uus_x,
                "y": uus_y,
                "kiirus": uus_kiirus
            }

    # Kui 100 korraga ei leitud head kohta,
    # siis loome auto lihtsalt juhuslikult,
    # et mäng kinni ei jääks
    return {
        "x": random.choice(ohutud_rajad),
        "y": random.randint(-600, -120),
        "kiirus": random.randint(4, 7)
    }


# Loome algsed sinised autod
for i in range(autode_arv):
    auto = loo_uus_auto(sinised_autod)
    sinised_autod.append(auto)

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

        # Liigutame autot alla
        auto["y"] += auto["kiirus"]

        # Kui auto jõuab alla, paneme ta uuesti üles
        if auto["y"] > korgus:
            skoor += 1
            uus_auto = loo_uus_auto(sinised_autod, i)
            auto["x"] = uus_auto["x"]
            auto["y"] = uus_auto["y"]
            auto["kiirus"] = uus_auto["kiirus"]

        # Joonistame sinise auto
        aken.blit(sinine_auto_pilt, (auto["x"], auto["y"]))

    # Skoori kuvamine
    skoori_tekst = font.render("Skoor: " + str(skoor), True, must)
    aken.blit(skoori_tekst, (20, 20))

    # Ekraani uuendamine
    pygame.display.update()
    kell.tick(60)

pygame.quit()
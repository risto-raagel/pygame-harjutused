import pygame  # impordime pygame'i

pygame.init()  # käivitame pygame'i

# Loome 300x300 akna
aken = pygame.display.set_mode((300, 300))

# Määrame akna pealkirja
pygame.display.set_caption("Foor - Risto Räägel")

kaib = True

while kaib:

    # Kontrollime akna sulgemist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kaib = False

    # Taust mustaks
    aken.fill((0, 0, 0))

    # Foori korpus
    pygame.draw.rect(aken, (150, 150, 150), (100, 20, 100, 260), 2)

    # Valge raam ümber korpuse
    #pygame.draw.rect(aken, (255, 255, 255), (118, 42, 64, 236), 2)

    # Foorituled
    pygame.draw.circle(aken, (255, 0, 0), (150, 65), 38)     # punane
    pygame.draw.circle(aken, (255, 255, 0), (150, 150), 38)  # kollane
    pygame.draw.circle(aken, (0, 255, 0), (150, 235), 38)    # roheline

    # Uuendame ekraani
    pygame.display.flip()

pygame.quit()
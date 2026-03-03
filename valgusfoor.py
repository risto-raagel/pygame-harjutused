import pygame  # impordime pygame teegi

pygame.init()  # käivitame pygame'i

# Loome 300x300 akna
aken = pygame.display.set_mode((300, 300))

# Määrame akna pealkirja
pygame.display.set_caption("Foor - Risto Räägel")

# Muutuja, mis hoiab programmi töös
kaib = True

# Peamine tsükkel
while kaib:

    # Kontrollime sündmusi (nt akna sulgemine)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kaib = False  # lõpetame programmi

    # Taust mustaks
    aken.fill((0, 0, 0))

    # Joonistame foori korpuse (hall ristkülik)
    pygame.draw.rect(aken, (180, 180, 180), (110, 40, 80, 220))

    # Joonistame kolm tuld (ringid)
    pygame.draw.circle(aken, (255, 0, 0), (150, 90), 30)    # punane
    pygame.draw.circle(aken, (255, 255, 0), (150, 150), 30) # kollane
    pygame.draw.circle(aken, (0, 255, 0), (150, 210), 30)   # roheline

    # Uuendame ekraani
    pygame.display.flip()

# Sulgeme pygame'i
pygame.quit()
import pygame
import random

# Seadistame mängu akna suuruse ja fondi
pygame.init()
aken = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ringide loendur: Risto Räägel")
font = pygame.font.SysFont("Arial", 30)

# Algseis
ringid = []
klikke = 0

running = True
while running:
    # Täidame tausta (Helesinine)
    aken.fill((153, 204, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            klikke += 1

            # Suurendame olemasolevaid ringe
            for r in ringid:
                r['radius'] += 10

            # Lisame uue ringi (event.pos annab koordinaadid otse)
            varv = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ringid.append({'pos': event.pos, 'color': varv, 'radius': 10})

            # Piirame ringide arvu kümneni
            if len(ringid) > 10:
                ringid.pop(0)

    # Joonistame kõik ekraanile
    for r in ringid:
        pygame.draw.circle(aken, r['color'], r['pos'], r['radius'], 2)

    # Kuvame loenduri
    tekst = font.render(f"Klikke kokku: {klikke}", True, (0, 0, 0))
    aken.blit(tekst, (20, 20))

    pygame.display.flip()

pygame.quit()
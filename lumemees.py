import pygame  # impordime pygame'i

pygame.init()  # käivitame pygame'i

# Loome 300x300 suuruse akna
aken = pygame.display.set_mode((300, 300))

# Määrame aknale pealkirja
pygame.display.set_caption("Lumemees - Risto Räägel")

# Muutuja, mis hoiab programmi töös
käib = True
while käib:
    # Akna sulgemise kontrollimine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            käib = False  # programmi lõpetamine

    # Värvime akna tausta mustaks
    aken.fill((0, 0, 0))

    # Joonistame lumememme, milleks kasutame kolme valget ringi
    pygame.draw.circle(aken, (255, 255, 255), (150, 220), 60)  # alumine osa
    pygame.draw.circle(aken, (255, 255, 255), (150, 145), 45)  # keskmine osa
    pygame.draw.circle(aken, (255, 255, 255), (150, 80), 30)  # pea

    # Joonistame silmad (mustad väikesed ringid
    pygame.draw.circle(aken, (0, 0, 0), (140, 72), 4)
    pygame.draw.circle(aken, (0, 0, 0), (160, 72), 4)

    # Joonistame nina, milleks saab olema punane kolnurk
    pygame.draw.polygon(aken, (255, 0, 0), [(150, 80), (150, 95), (165, 88)])

    # Uuendame ekraani
    pygame.display.flip()

# Sulgeme pygame'i
pygame.quit()


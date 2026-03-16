import pygame  # impordime pygame'i teegi

pygame.init()  # käivitame pygame'i


# Funktsioon, mis joonistab ruudustiku
def ruudustik(aken, suurus, read, veerud, varv, paksus):

    # Joonistame horisontaalsed jooned
    for r in range(read + 1):
        pygame.draw.line(
            aken,
            varv,
            (0, r * suurus),
            (veerud * suurus, r * suurus),
            paksus   # joone paksus
        )

    # Joonistame vertikaalsed jooned
    for v in range(veerud + 1):
        pygame.draw.line(
            aken,
            varv,
            (v * suurus, 0),
            (v * suurus, read * suurus),
            paksus   # joone paksus
        )


# Ruudu suurus pikslites
ruudu_suurus = 25

# Ridade ja veergude arv
read = 20
veerud = 30

# Joone paksus pikslites
joone_paksus = 2

# Loome akna suurusega 640x480
aken = pygame.display.set_mode((640, 480))

# Määrame aknale pealkirja
pygame.display.set_caption("Harjutamine")

# Muutuja, mis hoiab programmi töös
kaib = True

# Peamine programmitsükkel
while kaib:

    # Kontrollime sündmusi (nt akna sulgemine)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kaib = False

    # Täidame akna taustavärviga
    aken.fill((153, 255, 153))

    # Joonistame ruudustiku
    ruudustik(aken, ruudu_suurus, read, veerud, (255, 0, 0), joone_paksus)

    # Uuendame ekraani
    pygame.display.flip()

# Sulgeme pygame'i
pygame.quit()
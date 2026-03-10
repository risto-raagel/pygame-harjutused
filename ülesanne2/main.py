import pygame

pygame.init()

# Akna seaded
laius = 640
korgus = 480
aken = pygame.display.set_mode((laius, korgus))
pygame.display.set_caption("Ülesanne 2 - Risto Räägel")

# Laeme pildid
taust = pygame.image.load("bg_shop.png")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")

# Muudame suurused sobivaks
taust = pygame.transform.scale(taust, (640, 480))
seller = pygame.transform.scale(seller, (250, 300))
chat = pygame.transform.scale(chat, (260, 160))

# Font
font = pygame.font.SysFont("arial", 22, )

# Tekst
tekst = font.render("Tere, olen Risto Räägel", True, (255, 255, 255))

# Objektide asukohad
seller_x = 110
seller_y = 165

chat_x = 240
chat_y = 120

tekst_x = 275
tekst_y = 175

kaib = True
while kaib:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kaib = False

    # Joonistamine
    aken.blit(taust, (0, 0))
    aken.blit(seller, (seller_x, seller_y))
    aken.blit(chat, (chat_x, chat_y))
    aken.blit(tekst, (tekst_x, tekst_y))

    pygame.display.update()

pygame.quit()
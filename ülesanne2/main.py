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
font = pygame.font.SysFont("arial", 32, bold=True)

# Tekst
tekst = font.render("Tere, olen Risto", True, (255, 255, 255))

# Objektide asukohad
seller_x = 70
seller_y = 160

chat_x = 210
chat_y = 70

tekst_x = 255
tekst_y = 125

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
import pygame
import sys
import random

# Mängu akna seaded, värvid ja teksti stiil
pygame.init()

# Veendu, et sul on samas kaustas helifail, "taustamuusika.mp3"
pygame.mixer.music.load("taustamuusika.mp3")
pygame.mixer.music.play(-1) # -1 tähendab, et muusika kordub lõputult

SCREEN_SIZE = (640, 480)
LBLUE, WHITE = [153, 204, 255], [255, 255, 255]

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Ping-Pong Risto Räägel")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

score = 0

def reset_ball(rect):
    rect.x = random.randint(50, SCREEN_SIZE[0] - 50)
    rect.y = 20
    return random.choice([-4, 4]), 4

# Palli ja aluse laadimine
ball_img = pygame.transform.scale(pygame.image.load("ball-1.png"), (20, 20))
ball_rect = ball_img.get_rect()
ball_sp_x, ball_sp_y = reset_ball(ball_rect)

pad_img = pygame.transform.scale(pygame.image.load("pad.png"), (120, 20))
pad_rect = pad_img.get_rect(centerx=SCREEN_SIZE[0] // 2, y=SCREEN_SIZE[1] / 1.3)
pad_speed = 7 # Aluse kiirus klaviatuuriga liigutades

# Mängu peatsükkel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 1. KONTROLLI ALUST KLAVIATUURI ABIL
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pad_rect.left > 0:
        pad_rect.x -= pad_speed
    if keys[pygame.K_RIGHT] and pad_rect.right < SCREEN_SIZE[0]:
        pad_rect.x += pad_speed

    # Palli liikumine
    ball_rect.x += ball_sp_x
    ball_rect.y += ball_sp_y

    # Seinte põrked (Pall)
    if ball_rect.left <= 0 or ball_rect.right >= SCREEN_SIZE[0]:
        ball_sp_x *= -1
    if ball_rect.top <= 0:
        ball_sp_y *= -1

    # Kokkupõrge alusega
    if ball_rect.colliderect(pad_rect) and ball_sp_y > 0:
        ball_sp_y *= -1
        score += 1

    # 2. MÄNGU LÕPETAMINE, KUI PALL PUUDUTAB ALUMIST ÄÄRT
    if ball_rect.bottom >= SCREEN_SIZE[1]:
        print(f"Mäng läbi! Sinu skoor: {score}")
        pygame.time.delay(500)  # Väike paus (0.5 sek), et mängija saaks aru, et kaotas
        score = 0  # Nullime skoori
        ball_sp_x, ball_sp_y = reset_ball(ball_rect)  # Viime palli üles tagasi
        pad_rect.centerx = SCREEN_SIZE[0] // 2  # Viime aluse keskele tagasi

    # Joonistamine
    screen.fill(LBLUE)
    screen.blit(ball_img, ball_rect)
    screen.blit(pad_img, pad_rect)

    # Skoori kuvamine
    score_display = font.render(f"Skoor: {score}", True, WHITE)
    screen.blit(score_display, (10, 10))

    pygame.display.flip()
    clock.tick(60)
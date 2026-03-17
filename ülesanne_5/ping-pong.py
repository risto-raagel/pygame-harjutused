import pygame
import sys
import random

# Mängu akna seaded, värvid ja teksti stiil
pygame.init()
SCREEN_SIZE = (640, 480)
LBLUE, WHITE = [153, 204, 255], [255, 255, 255]

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Määrame seade, et skoor algab alati nullist
score = 0

# Funktsioonid
def reset_ball(rect):
    rect.x = random.randint(50, SCREEN_SIZE[0] - 50)
    rect.y = 20
    # Tagastab uue kiiruse (x, y)
    return random.choice([-4, 4]), 4

# Palli ja aluse laadimine
ball_img = pygame.transform.scale(pygame.image.load("ball-1.png"), (20, 20))
ball_rect = ball_img.get_rect()
ball_sp_x, ball_sp_y = reset_ball(ball_rect)

pad_img = pygame.transform.scale(pygame.image.load("pad.png"), (120, 20))
pad_rect = pad_img.get_rect(centerx=SCREEN_SIZE[0] // 2, y=SCREEN_SIZE[1] / 1.5)
pad_speed = 3

# Mängu peatsükkel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Liikumise loogika
    ball_rect.x += ball_sp_x
    ball_rect.y += ball_sp_y
    pad_rect.x += pad_speed

    # Seinte põrked (Pall)
    if ball_rect.left <= 0 or ball_rect.right >= SCREEN_SIZE[0]:
        ball_sp_x *= -1
    if ball_rect.top <= 0:
        ball_sp_y *= -1

    # Seinte põrked (Alus)
    if pad_rect.left <= 0 or pad_rect.right >= SCREEN_SIZE[0]:
        pad_speed *= -1

    # Kokkupõrge alusega
    if ball_rect.colliderect(pad_rect) and ball_sp_y > 0:
        ball_sp_y *= -1
        score += 1

    # Alumine äär (Death Zone) ja palli reset
    if ball_rect.bottom >= SCREEN_SIZE[1]:
        score -= 1
        ball_sp_x, ball_sp_y = reset_ball(ball_rect)

    # Joonistamine
    screen.fill(LBLUE)
    screen.blit(ball_img, ball_rect)
    screen.blit(pad_img, pad_rect)

    # Skoori kuvamine
    score_display = font.render(f"Skoor: {score}", True, WHITE)
    screen.blit(score_display, (10, 10))

    pygame.display.flip()
    clock.tick(60)
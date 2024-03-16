import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_y = min(ball_y + speed, HEIGHT - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_x - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + speed, WIDTH - ball_radius)

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

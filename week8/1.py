import pygame
import datetime
import sys
import os

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "mickeyclock.jpeg")
mickey_image = pygame.image.load(image_path)
mickey_rect = mickey_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.datetime.now().time()

    minutes_angle = -(current_time.minute * 6) 
    seconds_angle = -(current_time.second * 6)  

    mickey_minutes = pygame.transform.rotate(mickey_image, minutes_angle)
    mickey_seconds = pygame.transform.rotate(mickey_image, seconds_angle)

    screen.fill((255, 255, 255))

    screen.blit(mickey_minutes, mickey_minutes.get_rect(center=mickey_rect.center))
    screen.blit(mickey_seconds, mickey_seconds.get_rect(center=mickey_rect.center))

    pygame.display.flip()

    pygame.time.Clock().tick(30)




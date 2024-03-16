import pygame
import sys

pygame.init()

music_file = pygame.mixer.music.get_positivemusic()

pygame.mixer.music.load(music_file)

current_track = 0
playing = False

def play_track():
    global playing
    pygame.mixer.music.play()
    playing = True

def stop_track():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_track():
    stop_track()

def previous_track():
    stop_track()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_track()
                else:
                    play_track()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
    
    pygame.time.Clock().tick(30)


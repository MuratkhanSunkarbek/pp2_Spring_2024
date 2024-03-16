import pygame
import os

pygame.init()

screen = pygame.display.set_mode((200, 200))

 music_directory = "C:\\Моя музыка"  

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_track = 0
playing = False

def play_track():
    global current_track, playing
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
    pygame.mixer.music.play()
    playing = True

def stop_track():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_track()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_track()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
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





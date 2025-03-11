import pygame
import os

pygame.init()
pygame.mixer.init()


floder = ".\musics"  
songs = [f for f in os.listdir(floder) if f.endswith(".mp3")]
current_song_index = 0

def play_song():
    pygame.mixer.music.load(os.path.join(floder, songs[current_song_index]))
    pygame.mixer.music.play()
    print(f"Playing: {songs[current_song_index]}")

def stop_song():
    pygame.mixer.music.stop()
    print("Stopped")

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song()

if songs:
    play_song()

screen = pygame.display.set_mode((400, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Resumed")
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_b:
                prev_song()

pygame.quit()

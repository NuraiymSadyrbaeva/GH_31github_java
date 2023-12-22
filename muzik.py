import pygame
import time

def play_music(file_path):
    # Initialisiere Pygame
    pygame.init()
    
    # Lade die Musikdatei
    pygame.mixer.music.load(file_path)
    
    # Spiele die Musikdatei ab
    pygame.mixer.music.play()

    # Halte das Skript aktiv, bis die Musik zu Ende ist
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # Beende Pygame, nachdem die Musik abgespielt wurde
    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    # Passe den Dateipfad zu deiner Musikdatei an
    music_file_path = 'pfad/zur/musikdatei.mp3'
    play_music(music_file_path)

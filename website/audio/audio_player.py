import pygame
import time


class AudioPlayer():
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

    def play_sound(self, name):
        path = f"DHBW-Exit-Game/website/audio/audio_files/{name}.mp3"
        sound = pygame.mixer.Sound(path)
        sound.play()
        time.sleep(sound.get_length())


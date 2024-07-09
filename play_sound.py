import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import random

sound_files = ['1.wav', '2.wav', '3.wav', '4.wav', '5.wav']

def play_sound():
    pygame.mixer.init()
    selected_file = random.randint(0,4)
    pygame.mixer.music.load(sound_files[selected_file])
    pygame.mixer.music.play()

    time.sleep(3)  # Play the sound for 3 seconds
    pygame.mixer.music.stop()

if __name__ == "__main__":
    play_sound()

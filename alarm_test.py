import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load("alarm.wav")

print("Playing alarm...")


for i in range (3):

     pygame.mixer.music.play()
     time.sleep(2)

pygame.mixer.music.stop()

print("Alarm stopped.")
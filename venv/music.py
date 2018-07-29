import time
import pygame

file=r'1.mp3'
pygame.mixer.init()
rack = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(28)
pygame.mixer.music.stop()


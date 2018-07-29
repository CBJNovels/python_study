print("你好，世界")
import time
import pygame
file=r'D:\CloudMusic\Rainton桐 - 最后的旅行（纯歌版）.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(300)
pygame.mixer.music.stop()
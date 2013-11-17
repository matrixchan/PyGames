# -*- coding: utf-8 -*- 
import pygame, sys, time
from pygame.locals import *

pygame.init()
#return pygame.Surface object for the windows
#set het windows in pixels for 400,300
DISPLAYSURF = pygame.display.set_mode((400, 300))
#set the caption
pygame.display.set_caption('Play Sound')
soundObj = pygame.mixer.Sound('beeps.wav')

while True: # main game loop
    soundObj.play()
    time.sleep(1)
    soundObj.stop()
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
    pygame.display.update()


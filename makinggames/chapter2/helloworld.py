import pygame, sys
from pygame.locals import *
 
pygame.init()
'return pygame.Surface object for the windows
'set het windows in pixels for 400,300
DISPLAYSURF = pygame.display.set_mode((400, 300))
'set the caption
pygame.display.set_caption('Hello World!')
'
while True: # main game loop
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
     pygame.display.update()

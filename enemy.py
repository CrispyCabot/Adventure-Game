import pygame
from config import PATH
import os

dogSize = .7

img = pygame.image.load(PATH+os.path.join('data', 'enemies','dog', 'dog1.png'))
w, h = img.get_rect().size
img2 = pygame.image.load(PATH+os.path.join('data', 'enemies','dog', 'dog2.png'))
dogr = [pygame.transform.scale(img, (int(dogSize*w), int(dogSize*h))), 
        pygame.transform.scale(img2, (int(dogSize*w), int(dogSize*h)))]
class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frameCounter = 0

    def update(self, win):
        pos = dogr[int(self.frameCounter)].get_rect()
        pos.center = (self.x, self.y)
        win.blit(dogr[int(self.frameCounter)], pos)
        self.frameCounter += .2
        if self.frameCounter >= len(dogr):
            self.frameCounter = 0
import pygame
import os
from config import PATH, SIZE
def loadSprite2(folder, amt, char): #Left images
    for i in range(0, amt):
        img = pygame.transform.flip(pygame.image.load(PATH +
                                os.path.join('data', 'char', folder, 'tile00' + str(i)+'.png')), True, False)
        w, h = img.get_rect().size
        img = pygame.transform.scale(img, (int(SIZE * w), int(SIZE * h)))
        char[folder].append(img)

def loadSprite(folder, amt, char): #Right images
    for i in range(0, amt):
        img = pygame.image.load(PATH +
                                os.path.join('data', 'char', folder, 'tile00' + str(i)+'.png'))
        w, h = img.get_rect().size
        img = pygame.transform.scale(img, (int(SIZE * w), int(SIZE * h)))
        char[folder].append(img)

def loadR(char):
    loadSprite('death', 4, char)
    loadSprite('hurt', 5, char)
    loadSprite('idle', 4, char)
    loadSprite('longJump', 8, char)
    loadSprite('quickJump', 4, char)
    loadSprite('run', 3, char)
    loadSprite('slash', 4, char)
    loadSprite('sneak', 6, char)
    loadSprite('throw', 5, char)

def loadL(char):
    loadSprite2('death', 4, char)
    loadSprite2('hurt', 5, char)
    loadSprite2('idle', 4, char)
    loadSprite2('longJump', 8, char)
    loadSprite2('quickJump', 4, char)
    loadSprite2('run', 3, char)
    loadSprite2('slash', 4, char)
    loadSprite2('sneak', 6, char)
    loadSprite2('throw', 5, char)

charr = {
        'death': [],
        'hurt': [],
        'idle': [],
        'longJump': [],
        'quickJump': [],
        'run': [],
        'slash': [],
        'sneak': [],
        'throw': []
    }

charl = {
        'death': [],
        'hurt': [],
        'idle': [],
        'longJump': [],
        'quickJump': [],
        'run': [],
        'slash': [],
        'sneak': [],
        'throw': []
    }

loadR(charr)
loadL(charl)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.frameCounter = -1
        self.jumpMax = 20
        self.jumpVel = self.jumpMax
        self.dir = 'right'
        self.jump = False
        self.action = 'idle'
        self.lastAction = 'idle' #used to detect a change in action
    def update(self, win):
        if self.action == self.lastAction:
            self.frameCounter += 1
        else:
            self.frameCounter = 0
            self.lastAction = self.action
        if self.frameCounter >= len(charr[self.action]):
            self.frameCounter = -1
        if self.dir == 'right':
            img = charr[self.action][self.frameCounter]
        elif self.dir == 'left':
            img = charl[self.action][self.frameCounter]
        pos = img.get_rect()
        pos.center = self.x, self.y #Center anchor
        win.blit(img, pos)

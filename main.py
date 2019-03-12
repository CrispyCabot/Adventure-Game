import pygame
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE
import os
import time

from config import SCREEN_HEIGHT, SCREEN_WIDTH, PATH, SIZE
from player import Player

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #,pygame.FULLSCREEN
pygame.display.set_caption('blablksdjfkl')

clock = pygame.time.Clock()

def loadSprite(folder, amt, char):
    for i in range(0, amt):
        img = pygame.image.load(PATH +
                                os.path.join('data', 'char', folder, 'tile00' + str(i)+'.png'))
        w, h = img.get_rect().size
        img = pygame.transform.scale(img, (int(SIZE * w), int(SIZE * h)))
        char[folder].append(img)

def drawGame(player):
    pygame.draw.rect(win, (0,0,0), pygame.Rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT)) #clear screen
    #background
    player.update(win)

    pygame.display.update()

def main():
    playing = True
    screen = 'gameScreen'
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT-100)

    while playing:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        if screen == 'gameScreen':

            keys = pygame.key.get_pressed()
            player.action = 'idle'
            if keys[K_SPACE]:
                player.action = 'slash'
            else:
                if keys[K_RIGHT] and not keys[K_LEFT]:
                    player.x += 10
                    player.action = 'run'
                    player.dir = 'right'
                if keys[K_LEFT] and not keys[K_RIGHT]:
                    player.x -= 10
                    player.action = 'run'
                    player.dir = 'left'

            drawGame(player)

main()

pygame.quit()
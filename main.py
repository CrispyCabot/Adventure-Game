import pygame
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE
import os
import time

from config import SCREEN_HEIGHT, SCREEN_WIDTH, PATH, SIZE
from player import Player

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN) #,pygame.FULLSCREEN
pygame.display.set_caption('blablksdjfkl')

bg = []
for i in range(0, 54):
    bg.append(pygame.transform.scale(pygame.image.load(PATH+os.path.join('data', 'bg', 'tile'+str(i)+'.png')), (SCREEN_WIDTH, SCREEN_HEIGHT)))

clock = pygame.time.Clock()

def loadSprite(folder, amt, char):
    for i in range(0, amt):
        img = pygame.image.load(PATH +
                                os.path.join('data', 'char', folder, 'tile00' + str(i)+'.png'))
        w, h = img.get_rect().size
        img = pygame.transform.scale(img, (int(SIZE * w), int(SIZE * h)))
        char[folder].append(img)

def drawMain(frameCounter):
    win.blit(bg[frameCounter], (0,0))

def drawGame(player):
    player.update(win)

    pygame.display.update()

def main():
    playing = True
    screen = 'gameScreen'
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT-100)
    frameCounter = 0

    while playing:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        if screen == 'gameScreen':

            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                playing = False
            player.action = 'idle'
            if keys[K_SPACE]:
                player.action = 'slash'
            else:
                if player.jump:
                    player.jump = True
                    player.y -= player.jumpVel
                    player.jumpVel -= 4
                    player.action = 'longJump'
                    if player.dir == 'left':
                        player.x -= 10
                    if player.dir == 'right':
                        player.x += 10
                    if player.jumpVel <  -player.jumpMax:
                        player.jumpVel = player.jumpMax
                        player.jump = False
                else:
                    if keys[K_UP]:
                        player.jump = True
                        player.y -= player.jumpVel
                        player.jumpVel -= 4
                        player.action = 'longJump'
                        if player.dir == 'left':
                            player.x -= 10
                        if player.dir == 'right':
                            player.x += 10
                        if player.jumpVel <  -player.jumpMax:
                            player.jumpVel = player.jumpMax
                            player.jump = False
                    if keys[K_RIGHT] and not keys[K_LEFT]:
                        player.x += 10
                        player.action = 'run'
                        player.dir = 'right'
                    if keys[K_LEFT] and not keys[K_RIGHT]:
                        player.x -= 10
                        player.action = 'run'
                        player.dir = 'left'
            drawMain(frameCounter)
            frameCounter += 1
            if frameCounter >= 54:
                frameCounter = 0
            drawGame(player)

main()

pygame.quit()
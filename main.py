import pygame
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE
import os
import time

from config import SCREEN_HEIGHT, SCREEN_WIDTH, PATH, SIZE
from player import Player
from ledge import Platform

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN) #,pygame.FULLSCREEN
pygame.display.set_caption('cary is dumb')

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

def drawGame(player, frameCounter, platforms):
    win.blit(bg[frameCounter], (0,0))
    for i in platforms:
        i.update(win)
    player.update(win)

    pygame.display.update()

def main():
    playing = True
    screen = 'gameScreen'
    frameCounter = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT-100)
    platforms = [Platform(-50,SCREEN_HEIGHT-50, SCREEN_WIDTH+100, 100, 'floor'), 
                Platform(100,SCREEN_HEIGHT-200,200,30, 'plat'),
                Platform(100,SCREEN_HEIGHT-400,200,30, 'plat'),
                Platform(200, SCREEN_HEIGHT-200,200,30, 'plat')
                ]
    playerSpeed = 10

    while playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        if screen == 'gameScreen':
            player.lastY = player.y
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                playing = False
            player.action = 'idle'
            if player.jump:
                player.y -= player.jumpVel
                player.jumpVel -= 2
                if player.jumpVel < 0:
                    for i in platforms:
                        check, val = i.hit(player.x, player.y+player.height/2-10, player.lastY)
                        if check:
                            player.jump = False
                            player.y = val-player.height/2
                            player.jumpVel = player.jumpMax
            if keys[K_UP] and not player.jump:
                player.jump = True
                player.y -= player.jumpVel
                player.action = 'run' #the jump action is bad so yeah
                if player.jumpVel <  -player.jumpMax:
                    player.jumpVel = player.jumpMax
                    player.jump = False
            if keys[K_RIGHT] and not keys[K_LEFT]:
                player.x += playerSpeed
                if player.x > SCREEN_WIDTH:
                    player.x = SCREEN_WIDTH
                player.action = 'run'
                player.dir = 'right'
                for i in platforms:
                    check, val = i.hit(player.x, player.y+player.height/2-10, player.lastY)
                    if not(check) and not(player.jump):
                        player.jump = True
                        player.jumpVel = 0
            if keys[K_LEFT] and not keys[K_RIGHT]:
                player.x -= playerSpeed
                if player.x < 0:
                    player.x = 0
                player.action = 'run'
                player.dir = 'left'
                for i in platforms:
                    check, val = i.hit(player.x, player.y+player.height/2-10, player.lastY)
                    if not(check) and not(player.jump):
                        player.jump = True
                        player.jumpVel = 0
            if keys[K_SPACE]:
                player.action = 'slash'
            if keys[K_DOWN] and not player.jump:
                player.jump = True
                player.jumpVel = 0
                player.y += 10
                player.lastY = player.y
            frameCounter += .5
            if frameCounter >= 54:
                frameCounter = 0
            drawGame(player, int(frameCounter), platforms)

main()

pygame.quit()
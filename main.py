import pygame
import os

pygame.init()

width = 1920
height = 1080

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
#pygame.display.set_icon('')
PATH = os.path.abspath(__file__) #This gets the whole path so like: /Users/user/folder/Tanks/Tanks.py
PATH = PATH[0:-7] #-7 to chop off main.py
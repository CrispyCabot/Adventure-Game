import pygame

class Platform:
    def __init__(self, x, y, w, h, typee):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = typee
    def update(self, win):
        if self.type == 'floor':
            pass
        if self.type == 'plat':
            pygame.draw.rect(win, (0,255,0), pygame.Rect(self.x, self.y, self.w, self.h))
    def hit(self, x, y):
        if self.x < x and x < self.x+self.w and self.y < y and y < self.y+self.h:
            return True, self.y
        return False, 0
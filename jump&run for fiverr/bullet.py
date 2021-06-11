import pygame

class Bullets():

    def __init__(self, color):
        self.color = color
        self.bullets = []

    def show(self, win):
        for bullet in self.bullets:
            pygame.draw.rect(win, self.color, bullet)

    def create(self, rect):
        self.bullets.append(rect)

    def fade(self):
        pass
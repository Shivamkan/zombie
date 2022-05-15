import math

import pygame
from util import *

WIDTH = 50
HEIGHT = 50
SPEED = (0.1, 0.03)
COLOR = "#004506fff"


class Zombie:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, RGB(COLOR), (self.x, self.y, WIDTH, HEIGHT))

    def update(self, delta):
        deltaX = 375 - self.x
        if deltaX:
            sign = deltaX / math.fabs(deltaX)
            self.x += SPEED[0] * delta * sign
        deltaY = 225 - self.y
        if deltaY:
            sign = deltaY / math.fabs(deltaY)
            self.y += SPEED[1] * delta * sign

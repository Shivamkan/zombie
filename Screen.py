import sys
import pygame
from util import RGB


class Screen:

    def __init__(self, game, width=500, height=500):
        self.game = game
        self.width = width
        self.height = height
        self.size = self.width, self.height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width ,self.height + 60))
        self.event = None

    def update(self, delta):
        self.saveEvent()
        self.handleInput()
        self.screenChange()

    def render(self):
        self.renderStart()
        self.display()
        pygame.display.flip()

    def display(self):
        print(f"{type(self).__name__}: display not defined.")

    def renderStart(self):
        self.screen.fill((RGB("#000000")))

    def handleInput(self):
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()

    def saveEvent(self):
        self.event = pygame.event.get()

    def screenChange(self):
        pass

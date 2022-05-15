import pygame
from Screen import Screen
from util import *

class SettingScreen(Screen):

    def __init__(self, game, width=500, height=500):
        super().__init__(game, width, height)
        self.slider = pygame.Rect((self.width / 4 + 10, self.height / 6 + 10),
                                  (mapThis(self.game.speed, 0, 100, 0, self.width / 2 - 20),
                                   self.height / 8 - 20))
        self.speedSlider = pygame.Rect((width / 4, height / 6), (width / 2, height / 8))
        self.screenBut = pygame.Rect((self.width / 4), (self.height / 6) * 4, (self.width / 2), 50)

    def display(self):
        pygame.draw.rect(self.screen, (RGB("#555555")), self.speedSlider)
        pygame.draw.rect(self.screen, (RGB("#0000FF")), self.slider)
        pygame.draw.rect(self.screen, (RGB("#FF0000")), self.screenBut)

    def screenChange(self):
        for event in self.event:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.screenBut.collidepoint(event.pos) and event.button == 1:
                    self.game.changeScreen("GameScreen")
                elif self.speedSlider.collidepoint(event.pos) and event.button == 1:
                    self.game.speed = int(mapThis(event.pos[0], self.width / 4 + 10, (self.width / 4) * 3 - 10, 0, 100))
                    self.slider = pygame.Rect((self.width / 4 + 10, self.height / 6 + 10),
                                              (mapThis(self.game.speed, 0, 100, 0, self.width / 2 - 20),
                                               self.height / 8 - 20))

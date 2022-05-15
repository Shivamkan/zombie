import pygame
from Screen import Screen
from util import *


class TitleScreen(Screen):

    def __init__(self, game, width=500, height=500):
        super().__init__(game, width, height)
        font = pygame.font.SysFont(None, 70)
        font.set_bold(True)
        self.Title = font.render("Zombie Killer", 1, (100, 10, 10))
        self.Start = font.render("Start", 1, (100, 10, 10))
        self.Settings = font.render("Settings", 1, (100, 10, 10))
        self.screenButton = pygame.Rect((self.width / 4), (self.height / 6) * 4, (self.width / 2), 50)
        self.SettingsButton = pygame.Rect((self.width / 4), self.height, (self.width / 2), 50)
        self.textpos = self.Title.get_rect(centerx=self.screen.get_width() / 2, centery=self.screen.get_height() / 6)
        self.textpos2 = self.Start.get_rect(centerx=self.screen.get_width() / 2, centery=self.height / 3 * 2 + 25)

    def display(self):
        pygame.draw.rect(self.screen, RGB("#ff0066"), self.screenButton)
        pygame.draw.rect(self.screen, RGB("#00ff00"), self.SettingsButton)
        self.screen.blit(self.Title, self.textpos)
        self.screen.blit(self.Start, self.textpos2)
        self.screen.blit(self.Settings, self.SettingsButton)

    def screenChange(self):
        for event in self.event:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.screenButton.collidepoint(event.pos) and event.button == 1:
                    self.game.changeScreen("GameScreen")
                elif self.SettingsButton.collidepoint(event.pos) and event.button == 1:
                    self.game.changeScreen("SettingScreen")

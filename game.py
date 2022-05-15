import pygame
import Settings
import TitleScreen
import gamescreen

lastTime = pygame.time.get_ticks()
lag = 0


def delta():
    global lastTime
    current = pygame.time.get_ticks()
    delta = current - lastTime
    lastTime = current
    return delta


class Game:

    def __init__(self):
        self.speed = 20
        self.screens = {
            "GameScreen": gamescreen.GameScreen(self, 500, 500),
            "TitleScreen": TitleScreen.TitleScreen(self, 500, 500),
            "SettingScreen": Settings.SettingScreen(self, 500, 500)
        }
        self.currentScreen = self.screens["TitleScreen"]

    def changeScreen(self, name):
        self.currentScreen = self.screens[name]

    def run(self):
        self.currentScreen.render()
        self.currentScreen.update(delta())


game = Game()
while True:
    game.run()

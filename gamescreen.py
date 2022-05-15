import sys
from random import randint
import pygame
import Screen
from Zombie import Zombie
from util import *


class GameScreen(Screen.Screen):

    def __init__(self, game, width=500, height=500):
        super().__init__(game, width, height)
        self.reloadTimeLeft = 80
        self.PLAYERRECT = pygame.Rect((375, 225), (50, 50))
        self.screenBut = pygame.Rect((self.width / 4), self.height, (self.width / 2), 50)
        self.timeBetweenSpawn = 0
        self.zombie = Zombie(randint(0, 50), randint(0, 400))
        self.zombieList = [self.zombie]
        self.health = 5
        self.zombieKilled = 0
        self.maxAmmo = 5
        self.fire = 0
        self.bullettime = 50
        self.ammoLeft = self.maxAmmo

    def screenChange(self):
        for event in self.event:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.screenBut.collidepoint(event.pos[0], event.pos[1]):
                    self.game.changeScreen("SettingScreen")

    def reload(self):
        self.reloadTimeLeft -= 1
        if self.reloadTimeLeft == 0:
            self.ammoLeft = self.maxAmmo
            self.reloadTimeLeft = 80
            if self.zombieKilled >= 20:
                self.maxAmmo += 1
                self.zombieKilled = 0

    def drawammo(self):
        for i in range(self.ammoLeft):
            pygame.draw.rect(self.screen, RGB("#ffac00"), (((i + 1) * 15, 485), (10, 30)))
            pygame.draw.ellipse(self.screen, RGB("#ffac00"), (((i + 1) * 15, 475), (10, 30)))
            pygame.draw.rect(self.screen, RGB("#000000"), (((i + 1) * 15, self.width), (10, 30)))

    def handleInput(self):
        super().handleInput()
        for event in self.event:
            if event.type == pygame.QUIT:
                sys.exit()
            if self.ammoLeft >= 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ammoLeft -= 1
                    self.fire = 1
                    self.firePlace = event.pos
                    for zombie in self.zombieList:
                        if pygame.Rect(zombie.x, zombie.y, 50, 50).collidepoint(event.pos[0], event.pos[1]):
                            self.zombieList.remove(zombie)
                            self.zombieKilled += 1
            else:
                self.reload()

    def update(self, delta):
        super().update(delta)
        self.spawnZombie()
        self.updateZombie(delta)
        self.zombieKill()

    def player(self):
        if self.fire == 1:
            self.bullettime -= 1
            pygame.draw.line(self.screen, RGB("#ffac00"), self.firePlace, (400, 250))
            if self.bullettime <= 0:
                self.fire = 0
                self.bullettime = 50
        if self.health == 5:
            pygame.draw.rect(self.screen, RGB("#00ff00ff"), self.PLAYERRECT)
        elif self.health == 4:
            pygame.draw.rect(self.screen, RGB("#c0ee12ff"), self.PLAYERRECT)
        elif self.health == 3:
            pygame.draw.rect(self.screen, RGB("#eeaf00fff"), self.PLAYERRECT)
        elif self.health == 2:
            pygame.draw.rect(self.screen, RGB("#ee7200fff"), self.PLAYERRECT)
        elif self.health == 1:
            pygame.draw.rect(self.screen, RGB("#ff0000fff"), self.PLAYERRECT)
        pygame.draw.circle(self.screen, (RGB("#705050")), (400, 250), 20)

    def spawnZombie(self):
        spawnSpeed = 100 - self.game.speed
        self.timeBetweenSpawn += .1
        if self.timeBetweenSpawn >= spawnSpeed and len(self.zombieList) <= 20:
            self.zombie = Zombie(randint(0, 50), randint(0, 400))
            self.zombieList.append(self.zombie)
            self.timeBetweenSpawn = 0

    def updateZombie(self, delta):
        for zombie in self.zombieList:
            zombie.update(delta)

    def zombieKill(self):
        for zombie in self.zombieList:
            if pygame.Rect(zombie.x, zombie.y, 50, 50).colliderect(self.PLAYERRECT):
                self.health -= 1
                self.zombieList.remove(zombie)
                if self.health <= 0:
                    sys.exit()

    def zombieDraw(self):
        for zombie in self.zombieList:
            zombie.draw(self.screen)

    def display(self):
        self.zombieDraw()
        self.player()
        self.drawammo()
        pygame.draw.rect(self.screen, (RGB("#FF0000")), self.screenBut)

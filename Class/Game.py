import pygame.sprite
from Class.tower import Tower
from math import *
from Class.enemies import Enemies


class Game:
    def __init__(self):
        self.health = 1000
        self.health_max = 1000
        self.wave = -1
        self.gold = 100
        self.time = -1
        self.screen = [1920, 1250]
        self.emplacement = [[True, (390, 270)], [True, (390, 915)], [True, (900, 915)], [True, (1285, 400)]]
        self.all_zombie = pygame.sprite.Group()
        self.all_tower = pygame.sprite.Group()
        self.wave_group = {0: [True, [0, True], ],
                           1: [True, [20, True], [22, True]],
                           2: [True, [40, True], [42, True], [44, True]],
                           3: [True, [60, True], [62, True], [64, True], [66, True]],
                           4: [True, [80, True], [82, True], [84, True], [86, True], [88, True]]
                           }

    def check_emplacement(self, mouse_x, mouse_y):
        for i, coordonner in enumerate(self.emplacement):
            distance = sqrt((mouse_x - coordonner[1][0]) ** 2 + (mouse_y - coordonner[1][1]) ** 2)
            if distance <= 125 and self.gold >= 100:
                self.gold -= 100
                self.spawn_tower(i)

    def bar_health(self, surface):
        bar_red = (225, 0, 0)
        bar_black = (0, 0, 0)
        bar_pos_red = [0, 0, self.health * 1.92, 30]
        bar_pos_black = [0, 0, self.health_max * 1.92, 30]
        pygame.draw.rect(surface, bar_black, bar_pos_black)
        pygame.draw.rect(surface, bar_red, bar_pos_red)

    def dead(self):
        for zombie in self.all_zombie:
            if zombie.health <= 0:
                self.gold += zombie.gold
                self.all_zombie.remove(zombie)
            if zombie.rect.x == 1700 and zombie.rect.y == 100:
                self.health -= zombie.attack
                self.all_zombie.remove(zombie)

    def check_wave(self):
        if self.time % 20 == 0 and self.wave < 4:
            self.wave += 1
        if self.wave_group[self.wave][0]:
            nbr = len(self.wave_group[self.wave])
            for i in range(1, nbr):
                if self.time >= self.wave_group[self.wave][i][0] and self.wave_group[self.wave][i][1] == True:
                    self.wave_group[self.wave][i][1] = False
                    self.spawn_zombie()
                    if i == nbr - 1:
                        self.wave_group[self.wave][0] = False

    def spawn_zombie(self):
        zombie = Enemies()
        self.all_zombie.add(zombie)

    def spawn_tower(self, select):
        if self.emplacement[select][0]:
            self.emplacement[select][0] = False
            tower = Tower(self.emplacement[select][1][0], self.emplacement[select][1][1])
            self.all_tower.add(tower)

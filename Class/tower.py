import pygame
from Class.enemies import Enemies
from math import *


class Tower(pygame.sprite.Sprite):
    def __init__(self, x , y):
        super().__init__()
        self.attack = 20
        self.speed = 30
        self.reload = 10
        self.range = 300
        self.angle = 140
        self.image = pygame.image.load('img/tower.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def attack_enemies(self, all_zombie):
        self.reload += 1
        for zombie in all_zombie:
            distance = sqrt((self.rect.centerx - zombie.rect.centerx) ** 2 + (self.rect.centery - zombie.rect.centery) ** 2)
            if distance <= self.range and self.reload >= self.speed:
                self.calcul_angle(zombie, distance)
                zombie.health -= self.attack
                self.reload = 0

    def calcul_angle(self, zombie, distance):
        A_x = self.rect.x
        A_y = self.rect.y
        B_x = self.rect.x + self.range
        B_y = self.rect.y
        m = (B_y - A_y) / (B_x - A_x)
        angle_rad_p = radians(self.angle + 1)
        angle_rad_m = radians(self.angle - 1)

        C_x = A_x + (distance * cos(angle_rad_p))
        C_y = A_y + (distance * sin(angle_rad_p))

        distance_p = sqrt((C_x - zombie.rect.centerx) ** 2 + (C_y - zombie.rect.centery) ** 2)

        C_x = A_x + (distance * cos(angle_rad_m))
        C_y = A_y + (distance * sin(angle_rad_m))

        distance_m = sqrt((C_x - zombie.rect.centerx) ** 2 + (C_y - zombie.rect.centery) ** 2)
        if distance_p != distance_m:
            if distance_p > distance_m:
                self.angle += 10
            else:
                self.angle -= 10
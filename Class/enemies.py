import pygame


class Enemies(pygame.sprite.Sprite):

    def __init__(self, health_max=100, velocity=5, attack=100):
        super().__init__()
        self.health = health_max
        self.health_max = health_max
        self.attack = attack
        self.gold = 15
        self.velocity = velocity
        self.image = pygame.image.load('img/zombie1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 1200
        self.chemin = {0: [150, 150, 90], 1: [670, 150, 0], 2: [670, 1050, -90], 3: [1050, 1050, 0], 4: [1050, 150, 90], 5: [1450, 150, 0],
                       6: [1450, 1050, -90], 7: [1700, 1050, 0], 8: [1700, 100, 90]}
        self.pos = 0

    def move(self):
        if self.pos == 9:
            return self.attack
        if self.chemin[self.pos][0] == self.rect.x and self.chemin[self.pos][1] == self.rect.y:
            self.pos += 1
            return 0
        if self.chemin[self.pos][0] != self.rect.x:
            if self.chemin[self.pos][0] > self.rect.x:
                self.rect.x += self.velocity
            else:
                self.rect.x -= self.velocity

        if self.chemin[self.pos][1] != self.rect.y:
            if self.chemin[self.pos][1] > self.rect.y:
                self.rect.y += self.velocity
            else:
                self.rect.y -= self.velocity
        return 0

    def bar_health(self, surface):
        bar_red = (225, 0, 0)
        bar_black = (0, 0, 0)
        bar_pos_red = [self.rect.x - 5, self.rect.y - 10, self.health / 1.5, 7]
        bar_pos_black = [self.rect.x - 5, self.rect.y - 10, self.health_max / 1.5, 7]
        pygame.draw.rect(surface, bar_black, bar_pos_black)
        pygame.draw.rect(surface, bar_red, bar_pos_red)

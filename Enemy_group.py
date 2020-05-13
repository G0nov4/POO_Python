import pygame
import random

class enemy_group:
    def __init__(self, enemy_num):
        self.enemy_size = 50
        self.enemy_Imga = [pygame.image.load('img/enemy1_1.png'),
                           pygame.image.load('img/enemy2_1.png'),
                           pygame.image.load('img/enemy3_1.png')]

        self.enemy_Img = []
        self.enemy_pos = []
        self.enemyX_change = []

        self.enemyY_change = 40
        self.vel_enemy = []
        self.num_enemy = enemy_num

        for i in range(self.num_enemy):
            Img_e = pygame.transform.scale(self.enemy_Imga[random.randint(0,2)], (self.enemy_size, self.enemy_size))
            self.enemy_Img.append(Img_e)
            self.enemy_pos.append([random.randint(0, 750), random.randint(40, 150)])
            self.enemyX_change.append(3)
            self.vel_enemy.append(random.randint(5, 10))

    def enemy_init(self, x, y, i, screen):
        screen.blit(self.enemy_Img[i], (x, y))

    def enemy_update(self, i):

        if self.enemy_pos[i][0] <= 0:
            self.enemyX_change[i] = self.vel_enemy[i]
            self.enemy_pos[i][1] += self.enemyY_change

        elif self.enemy_pos[i][0] >= 750:
            self.enemyX_change[i] = -self.vel_enemy[i]
            self.enemy_pos[i][1] += self.enemyY_change

        self.enemy_pos[i][0] += self.enemyX_change[i]


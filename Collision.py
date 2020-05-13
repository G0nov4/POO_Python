import pygame
import math
import random

class collision:

    @staticmethod
    def enemy_bum_bullet(enemigox, enemigoy, balaX ,balaY):
        distancia = math.sqrt((math.pow(enemigox-balaX, 2)) + (math.pow(enemigoy-balaY, 2)))
        if distancia < 10:
            return True
        else:
            return False

    @staticmethod
    def detectar_colision(enemigo_posX, enemigo_posY, x, y, enemigo_size):
        jx = x
        jy = y
        ex = enemigo_posX
        ey = enemigo_posY
        if (ex >= jx and ex < (jx + 10)) or (jx >= ex and jx < (ex + 27)):
            if (ey >= jy and ey < (jy + 10)) or (jy >= ey and jy < (ey + 27)):
                return True
        else:
            return False

    @classmethod
    def reset(self, bullet, enemy, conf, i):
        bullet.bullet_pos[1] = 500
        bullet.bullet_state = "ready"
        enemy.enemy_pos[i] = [random.randint(0, 750), random.randint(30, 150)]
        conf.score += 1
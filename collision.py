import pygame
import math
import random


class Collision:


    @staticmethod
    def enemy_bum_bullet(enemigo_x, enemigo_y, bala_X ,bala_Y):
        distancia = math.sqrt((math.pow(enemigo_x - bala_X, 2)) + (math.pow(enemigo_y - bala_Y, 2)))
        return distancia < 10


    @staticmethod
    def detectar_colision(enemigo_pos_X, enemigo_pos_Y, posicion_x, posicion_y, enemigo_size):
        punta_x_player = posicion_x
        punta_y_player = posicion_y
        punta_x_enemy = enemigo_pos_X
        punta_y_enemy = enemigo_pos_Y
        if (punta_x_enemy >= punta_x_player and punta_x_enemy < (punta_x_player + 10)) or (punta_x_player >= punta_x_enemy and punta_x_player < (punta_x_enemy + 27)):
            if (punta_y_enemy >= punta_y_player and punta_y_enemy < (punta_y_player + 10)) or (punta_y_player >= punta_y_enemy and punta_y_player < (punta_y_enemy + 27)):
                return True
        else:
            return False


    @classmethod
    def reset(cls, bullet, enemy, conf, i):
        bullet.bullet_pos[1] = 500
        bullet.bullet_state = "ready"
        enemy.enemy_pos[i] = [random.randint(0, 750), random.randint(30, 150)]
        conf.score += 1
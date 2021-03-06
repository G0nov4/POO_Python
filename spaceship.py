import pygame
import random

class Ship():


    def __init__(self, ANCHO, ALTO):
        self.ship_size = 50
        ship_image = pygame.image.load('img/nave1.png')
        self.ship_image = pygame.transform.scale(ship_image, (self.ship_size, self.ship_size))
        self.ship_X = ANCHO / 2
        self.ship_Y = ALTO - (self.ship_size * 2)
        self.ship_speed = 5


    def ship_player(self, posicion_x, posicion_y, ventana):
        ventana.blit(self.ship_image, (posicion_x, posicion_y))


    def movement_ship(self, vel, ANCHO):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.ship_X > 0:
            self.ship_X -= vel
        if keys[pygame.K_RIGHT] and self.ship_X <  ANCHO - self.ship_size:
            self.ship_X += vel




import pygame
import random
import Settings
class ship():
    def __init__(self, ANCHO, ALTO):
        self.ship_size = 50

        ship_image = pygame.image.load('img/nave1.png')
        self.ship_image = pygame.transform.scale(ship_image, (self.ship_size, self.ship_size))

        self.shipX = ANCHO / 2
        self.shipY = ALTO - (self.ship_size * 2)

        self.ship_speed = 5

    def ship_player(self, x, y, ventana):
        ventana.blit(self.ship_image, (x, y))

    def movement_ship(self, vel, ANCHO):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.shipX > 0:
            self.shipX -= vel
        if keys[pygame.K_RIGHT] and self.shipX <  ANCHO - self.ship_size:
            self.shipX += vel




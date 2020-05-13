import pygame

class bullet:
    def __init__(self):
        self.bullet_Img = pygame.image.load('img/laser2.png')
        self.bullet_Img = pygame.transform.scale(self.bullet_Img, (7, 25))

        self.bullet_pos = [0, 500]
        #self.bulletX_change = 0
        self.bulletY_change = 15

        self.bullet_state = "ready"  # Ready: listo para disparar  fuego: esta en proceso de ataque

    def bullet_movement(self, shipX, screen, sound_ship):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.bullet_state is "ready":
                sound_ship.play()
                self.bullet_pos[0] = shipX
                self.fire_bullet(self.bullet_pos[0], self.bullet_pos[1], screen)

    def bullet_update(self, screen):
        if self.bullet_pos[1] <= 0:
            self.bullet_pos[1] = 500
            self.bullet_state = "ready"

        if self.bullet_state is "fire":
            self.fire_bullet(self.bullet_pos[0], self.bullet_pos[1], screen)
            self.bullet_pos[1] -= self.bulletY_change

    def fire_bullet(self, x, y, screen):
            self.bullet_state = "fire"
            screen.blit(self.bullet_Img, (x + 23, y + 10))




import pygame

class Setting:

    def __init__(self):
        # Screen settings
        self.widht = 800
        self.heigth = 600
        self.widht_x_heigth = (self.widht, self.heigth)

        # Background settings
        background_load = pygame.image.load('img/background2.jpg')
        self.background = pygame.transform.scale(background_load, (800, 600))

        # Icon title settings
        self.icon = pygame.image.load('img/nave2.png')
        self.title = "Space Invaders"

        # velocidad de la nave
        self.ship_speed = 10

        # número de enemigos
        self.num_enemy = 15

        # Score Settings
        self.score = 0
        self.text_X = 250
        self.text_Y= 250

    def background_update(self, ventana):
        ventana.blit(self.background, (0,0))

    def load_icon_title(self):
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

    def load_sounds(self):
        self.ship_sound = pygame.mixer.Sound("sound/shoot.wav")
        self.enemy_killed_sound = pygame.mixer.Sound("sound/invaderkilled.wav")
        self.ship_sound.set_volume(0.1)
        self.enemy_killed_sound.set_volume(0.2)
        return self.ship_sound, self.enemy_killed_sound
    # Cargar lista de imagenes

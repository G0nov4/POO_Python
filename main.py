import pygame
import sys
from settings import Setting
from spaceship import Ship
from enemygroup import EnemyGroup
from bullet import Bullet
from collision import Collision
from text import Text

# Inicio de el paquete pygame
pygame.init()
pygame.mixer.init()

# Configuraciones
conf = Setting()

# Configuracion del sonido
sound_ship, sound_enemy = conf.load_sounds()

# Elementos de la ventana
screen = pygame.display.set_mode(conf.widht_x_heigth)

# Elementos de Texto
text = Text()
conf.load_icon_title()

# Iniciamos la nave con un inicio en las posiciones X y Y
# con los parametros de las configuraciones
ship = Ship(conf.widht, conf.heigth)

# Iniciamos los enemigos con el tamaño difinido en settings
enemy = EnemyGroup(conf.num_enemy)

# Iniciamos la municion de la nave
bullet = Bullet()

# Verifica inicio del juego
run_game = True

clock = pygame.time.Clock()
while run_game:
    # configuracion de pantalla
    conf.background_update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Funcion para la municion de la nave
    bullet.bullet_movement(ship.ship_X, screen, sound_ship)
    bullet.bullet_update(screen)

    # Funcion de la nave
    ship.movement_ship(conf.ship_speed, conf.widht)
    ship.ship_player(ship.ship_X, ship.ship_Y, screen)

    #funcion de los enemigos
    for i in range(conf.num_enemy):
        text.enemy_ship(enemy , conf.text_X, conf.text_Y, conf.score, screen, i)
        enemy.enemy_update(i)
        enemy.enemy_init(enemy.enemy_pos[i][0], enemy.enemy_pos[i][1], i, screen)
        # verificamos si hay colision
        #colision = collision.enemy_bum_bullet(enemy.enemy_pos[i][0], enemy.enemy_pos[i][1],
        #                           bullet.bullet_pos[0], bullet.bullet_pos[1])
        colision = Collision.detectar_colision(enemy.enemy_pos[i][0], enemy.enemy_pos[i][1],
                                               bullet.bullet_pos[0], bullet.bullet_pos[1],
                                               enemy.enemy_size)
        if colision:
            Collision.reset(bullet, enemy, conf, i)
            sound_enemy.play()

    text.show_score(conf, 20, 20, screen)
    pygame.display.update()
    clock.tick(30)

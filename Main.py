import pygame
import sys
from Settings import settings
from spaceship import ship
from Enemy_group import enemy_group
from Bullet import bullet
from Collision import collision
from Text import text
# Inicio de el paquete pygame
pygame.init()
pygame.mixer.init()

# Configuraciones
conf = settings()

# Configuracion del sonido
sound_ship, sound_enemy = conf.load_sounds()

# Elementos de la ventana
screen = pygame.display.set_mode(conf.w_x_h)

# Elementos de Texto
text = text()
conf.load_icon_title()

# Iniciamos la nave con un inicio en las posiciones X y Y
# con los parametros de las configuraciones
ship = ship(conf.widht, conf.heigth)

# Iniciamos los enemigos con el tamaño difinido en settings
enemy = enemy_group(conf.num_enemy)

# Iniciamos la municion de la nave
bullet = bullet()

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
    bullet.bullet_movement(ship.shipX, screen, sound_ship)
    bullet.bullet_update(screen)

    # Funcion de la nave
    ship.movement_ship(conf.ship_speed, conf.widht)
    ship.ship_player(ship.shipX, ship.shipY, screen)

    #funcion de los enemigos
    for i in range(conf.num_enemy):

        text.enemy_ship(enemy , conf.textX, conf.textY, conf.score, screen, i)

        enemy.enemy_update(i)
        enemy.enemy_init(enemy.enemy_pos[i][0], enemy.enemy_pos[i][1], i, screen)

        # verificamos si hay colision
        #colision = collision.enemy_bum_bullet(enemy.enemy_pos[i][0], enemy.enemy_pos[i][1],
        #                           bullet.bullet_pos[0], bullet.bullet_pos[1])
        colision = collision.detectar_colision(enemy.enemy_pos[i][0], enemy.enemy_pos[i][1],
                                              bullet.bullet_pos[0], bullet.bullet_pos[1],
                                               enemy.enemy_size)
        if colision:
            collision.reset(bullet, enemy, conf, i)
            sound_enemy.play()

    text.show_score(conf, 20, 20, screen)
    pygame.display.update()
    clock.tick(30)

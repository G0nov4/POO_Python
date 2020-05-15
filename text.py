import pygame

class Text:


    def __init__(self):
        self.font = pygame.font.Font('Fonts/space_invaders.ttf', 32)
        self.font_end_game = pygame.font.Font('Fonts/space_invaders.ttf', 64)
        self.font_end_game_score = pygame.font.Font('Fonts/space_invaders.ttf', 40)


    def end_game(self, x, y, score, screen):
        end_game_screen = self.font_end_game.render("END GAME", True, (255, 255, 255))
        score_screen = self.font_end_game_score.render("SCORE: "+ str(score) , True, (255, 255, 255))
        screen.blit(end_game_screen, (x, y))
        screen.blit(score_screen, (x + 50, y + 80))


    def enemy_ship(self, enemy, text_x_end, text_y_end, score ,screen, i):
        if enemy.enemy_pos[i][1] > 450:
            for j in range(enemy.num_enemy):
                enemy.enemy_pos[j][1] = 2000
            self.end_game(text_x_end, text_y_end, score, screen)


    def show_score(self, conf, position_x, position_y, ventana):
        score = self.font.render("Score : " + str(conf.score), True, (255, 255, 255))
        ventana.blit(score, (position_x, position_y))
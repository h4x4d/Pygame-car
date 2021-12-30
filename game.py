import pygame
import time
from exc import FinishException
from board import board_creator
from loader import load_image
from settings.constants import SIZE


class Game:
    def __init__(self, screen, car):
        self.screen = screen

        self.image = pygame.transform.scale(load_image('process.png', -2), SIZE)
        screen.blit(self.image, (0, 0))

        self.all_sprites = pygame.sprite.Group()
        self.car = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.board = pygame.sprite.Group()

        self.pause_button = pygame.Rect(950, 35, 100, 100)

        self.field_boards = pygame.sprite.Group()
        board_creator(car, self.all_sprites, self.screen, self.car, self.coins, self.board)

        self.screen.blit(self.image, (0, 0))

    def update(self):
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.update()
        self.board.draw(self.screen)
        try:
            self.board.update(self.screen, self.car)
        except FinishException:
            return 'finish'
        self.all_sprites.draw(self.screen)

        self.screen.blit(self.image, (0, 0))
        self.coins.draw(self.screen)

    def update_car(self, value, state):
        try:
            self.car.update(state, value)
        except FinishException:
            return 'finish'

    def timer(self):
        for i in range(3, -1, -1):
            font = pygame.font.Font('fonts/result-font2.ttf', 70)
            t = font.render(f'{i}', False, 'white')
            text_rect = t.get_rect(center=(SIZE[0] / 2, 330))
            time.sleep(0.5)

            self.screen.blit(self.image, (0, 0))
            self.board.draw(self.screen)
            self.car.draw(self.screen)
            self.coins.draw(self.screen)
            if i != 0:
                self.screen.blit(t, text_rect)
            pygame.display.flip()

